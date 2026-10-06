// SkillBridge Frontend API Client
// Connects to Flask REST backend with graceful local fallback if backend is offline.

const API_BASE_URL = "http://localhost:5000/api";

const SkillBridgeAPI = {
  isBackendAvailable: null,

  async checkBackend() {
    if (this.isBackendAvailable !== null) return this.isBackendAvailable;
    try {
      const res = await fetch(`${API_BASE_URL}/health`, { signal: AbortSignal.timeout(1200) });
      this.isBackendAvailable = res.ok;
    } catch (e) {
      this.isBackendAvailable = false;
    }
    return this.isBackendAvailable;
  },

  async login(email, password) {
    if (await this.checkBackend()) {
      try {
        const res = await fetch(`${API_BASE_URL}/auth/login`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email, password })
        });
        if (res.ok) {
          const data = await res.json();
          return data.user;
        }
      } catch (e) {
        console.warn("Backend login failed, using local simulation", e);
      }
    }
    // Local simulation
    const lowered = (email || "").toLowerCase();
    if (lowered.includes("orbis")) {
      return { role: "industry", orgId: "c_orbis", name: "Orbis Analytics", email };
    } else if (lowered.includes("kestrel")) {
      return { role: "industry", orgId: "c_kestrel", name: "Kestrel Retail Tech", email };
    } else if (lowered.includes("university") || lowered.includes(".edu")) {
      if (lowered.includes("student")) {
        return { role: "student", orgId: "s_meera", name: "Meera Iyer", email };
      }
      return { role: "university", orgId: "u_you", name: "Your University", email };
    }
    return { role: "student", orgId: "s_meera", name: "Meera Iyer", email };
  },

  async getStudentProfile() {
    if (await this.checkBackend()) {
      try {
        const res = await fetch(`${API_BASE_URL}/student/profile`);
        if (res.ok) return await res.json();
      } catch (e) {}
    }
    return null; // Fallback to state
  },

  async getOpportunities() {
    if (await this.checkBackend()) {
      try {
        const res = await fetch(`${API_BASE_URL}/student/opportunities`);
        if (res.ok) return await res.json();
      } catch (e) {}
    }
    return null;
  },

  async extractSkills(text) {
    if (await this.checkBackend()) {
      try {
        const res = await fetch(`${API_BASE_URL}/student/resume/extract`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ text })
        });
        if (res.ok) return await res.json();
      } catch (e) {}
    }
    // Client-side fallback NLP
    const catalog = ["Python", "SQL", "Machine Learning", "Pandas", "NumPy", "Scikit-learn", "Docker", "Git", "AWS", "REST APIs", "Data Visualization", "Communication"];
    const lowered = text.toLowerCase();
    const matched = catalog.filter(s => lowered.includes(s.toLowerCase()));
    return { extracted_skills: matched, count: matched.length };
  },

  async getPositions(companyId) {
    if (await this.checkBackend()) {
      try {
        const url = companyId ? `${API_BASE_URL}/company/positions?company_id=${companyId}` : `${API_BASE_URL}/company/positions`;
        const res = await fetch(url);
        if (res.ok) return await res.json();
      } catch (e) {}
    }
    return null;
  },

  async getCandidates(positionId, companyId) {
    if (await this.checkBackend()) {
      try {
        const res = await fetch(`${API_BASE_URL}/company/positions/${positionId}/candidates?company_id=${companyId}`);
        if (res.ok) {
          const data = await res.json();
          return data.candidates;
        }
      } catch (e) {}
    }
    return null;
  },

  async toggleShortlist(companyId, candidateId, isShortlisted, feedback) {
    if (await this.checkBackend()) {
      try {
        await fetch(`${API_BASE_URL}/company/shortlist`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ company_id: companyId, candidate_id: candidateId, is_shortlisted: isShortlisted, feedback })
        });
      } catch (e) {}
    }
    return true;
  },

  async getDemand() {
    if (await this.checkBackend()) {
      try {
        const res = await fetch(`${API_BASE_URL}/university/demand`);
        if (res.ok) return await res.json();
      } catch (e) {}
    }
    return null;
  },

  async refreshDemand() {
    if (await this.checkBackend()) {
      try {
        const res = await fetch(`${API_BASE_URL}/university/demand/refresh`, { method: "POST" });
        if (res.ok) return await res.json();
      } catch (e) {}
    }
    return null;
  },

  async getBenchmark() {
    if (await this.checkBackend()) {
      try {
        const res = await fetch(`${API_BASE_URL}/university/benchmark`);
        if (res.ok) return await res.json();
      } catch (e) {}
    }
    return null;
  }
};

window.SkillBridgeAPI = SkillBridgeAPI;
