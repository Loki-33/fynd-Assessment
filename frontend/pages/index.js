import { useEffect } from "react";
import { useRouter } from "next/router";

export default function Home() {
  const router = useRouter();

  useEffect(() => {
    router.replace("/user"); // redirect to user dashboard
  }, []);

  return <p>Redirecting...</p>;
}
