function RecommendationTable() {
  const data = [
    { id: 100001, risk: "High Risk", action: "Initiate recovery call" },
    { id: 100002, risk: "Medium Risk", action: "Send reminder" }
  ];

  return (
    <table border="1">
      <thead>
        <tr>
          <th>Customer ID</th>
          <th>Risk Band</th>
          <th>Recommended Action</th>
        </tr>
      </thead>
      <tbody>
        {data.map(row => (
          <tr key={row.id}>
            <td>{row.id}</td>
            <td>{row.risk}</td>
            <td>{row.action}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default RecommendationTable;