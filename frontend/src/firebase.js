import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyAnbaVaQvKBcqg8yKLkEA2zloQWDTXMPqU",
  authDomain: "ai-content-hub-3c130.firebaseapp.com",
  projectId: "ai-content-hub-3c130",
  storageBucket: "ai-content-hub-3c130.appspot.com", // corrected
  messagingSenderId: "875414090300",
  appId: "1:875414090300:web:b3b58b10a1393495dc0939",
  measurementId: "G-SJ2ZR8MEWP"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

export { auth };
