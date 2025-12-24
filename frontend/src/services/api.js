// frontend/services/api.js
// API service layer for CreditPathAI frontend

const API_BASE_URL = "http://localhost:8000"; // FastAPI endpoint (prototype)

// Function to get risk prediction
export async function getRiskRecommendation(riskScore) {
  try {
    const response = await fetch(`${API_BASE_URL}/predict`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        risk_score: riskScore,
      }),
    });

    if (!response.ok) {
      throw new Error("API request failed");
    }

    const data = await response.json();
    return data;

  } catch (error) {
    console.error("API Error:", error);
    return {
      risk_band: "Unavailable",
      recommended_action: "API connection failed",
    };
  }
}