export default function ReviewList({ reviews }) {
  if (!reviews.length) return <p>No reviews yet.</p>;

  return (
    <table border="1" style={{ width: "100%", marginTop: 20, borderCollapse: "collapse" }}>
      <thead>
        <tr>
          <th>RATING</th>
          <th>USER REVIEW</th>
          <th>AI SUMMARY</th>
          <th>AI RECOMMENDED ACTIONS</th>
          <th>CREATED AT</th>
        </tr>
      </thead>
      <tbody>
        {reviews.map((r, idx) => (
          <tr key={idx}>
            <td style={{ textAlign: "center" }}>{r.rating}</td>
            <td>{r.review}</td>
            <td>{r.ai_summary}</td>
            <td>{r.ai_actions}</td>
            <td>{new Date(r.created_at).toLocaleString()}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

