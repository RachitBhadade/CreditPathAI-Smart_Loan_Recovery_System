import Plot from "react-plotly.js";

function RiskDashboard() {
  return (
    <Plot
      data={[
        {
          values: [55, 25, 20],
          labels: ["Low Risk", "Medium Risk", "High Risk"],
          type: "pie"
        }
      ]}
      layout={{ title: "Borrower Risk Distribution" }}
    />
  );
}

export default RiskDashboard;