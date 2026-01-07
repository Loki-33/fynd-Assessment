import { useState } from "react";
import axios from "axios";

export default function ReviewForm({ onSuccess }) {
  const [rating, setRating] = useState(5);
  const [review, setReview] = useState("");
  const [aiResponse, setAiResponse] = useState("");

  const handleSubmit = async () => {
    if (!review.trim()) return alert("Write something!");

    try {
      const res = await axios.post(
        `${process.env.NEXT_PUBLIC_API_URL}/reviews/submit`,
        { rating, review }
      );
      setAiResponse(res.data.ai_response);
      setReview("");
      onSuccess && onSuccess();
    } catch (err) {
      console.error(err);
      alert("Submission failed.");
    }
  };

  return (
    <div style={{ maxWidth: 600, margin: "0 auto", textAlign: "center" }}>
      <div>
        <label>Rating: </label>
        <select value={rating} onChange={(e) => setRating(Number(e.target.value))}>
          {[1, 2, 3, 4, 5].map((n) => (
            <option key={n} value={n}>{n}</option>
          ))}
        </select>
      </div>

      <div style={{ marginTop: 20 }}>
        <textarea
          value={review}
          onChange={(e) => setReview(e.target.value)}
          rows={5}
          style={{ width: "100%" }}
          placeholder="Write your review..."
        />
      </div>

      <button onClick={handleSubmit} style={{ marginTop: 20 }}>Submit</button>

      {aiResponse && (
        <div style={{ marginTop: 20, border: "1px solid #ccc", padding: 10 }}>
          <h3>AI Response:</h3>
          <p>{aiResponse}</p>
        </div>
      )}
    </div>
  );
}

