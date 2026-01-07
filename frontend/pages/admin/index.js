import { useEffect, useState } from "react";
import axios from "axios";
import Header from "../../components/Header";
import ReviewList from "../../components/ReviewList";

export default function AdminDashboard() {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    const fetchReviews = async () => {
      try {
        const res = await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/reviews/list`);
        setReviews(res.data.reviews);
      } catch (err) {
        console.error(err);
      }
    };

    fetchReviews();
    const interval = setInterval(fetchReviews, 5000); 
    return () => clearInterval(interval);
  }, []);

  const ratingCounts = reviews.reduce((acc, r) => {
    acc[r.rating] = (acc[r.rating] || 0) + 1;
    return acc;
  }, {});

  return (
    <div style={{ maxWidth: 900, margin: "50px auto" }}>
      <Header title="Admin Dashboard" />

      <div>
        <h3>Review Counts by Rating:</h3>
        <ul>
          {Object.entries(ratingCounts).map(([rating, count]) => (
            <li key={rating}>⭐ {rating}: {count}</li>
          ))}
        </ul>
      </div>

      <ReviewList reviews={reviews} />
    </div>
  );
}
