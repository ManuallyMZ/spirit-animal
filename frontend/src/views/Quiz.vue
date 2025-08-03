<template>
  <div class="quiz-container shadow p-6 mx-auto text-center card">
    <h2>
      <b>Question {{ currentQuestionIndex + 1 }} of {{ questions.length }}</b>
    </h2>
    <p>{{ questions[currentQuestionIndex].text }}</p>
    <div class="flex flex-row gap-3 mt-2 button-container">
      <div
        v-for="option in questions[currentQuestionIndex].options"
        :key="option"
        class="mb-2"
      >
        <label>
          <button
            @click="handleAnswer(option)"
            :class="{
              'bg-blue-500 text-white font-bold py-2 px-4 rounded hover:bg-blue-600':
                answers[questions[currentQuestionIndex].id] === option,
            }"
          >
            {{ option }}
          </button>
        </label>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";
const router = useRouter();
const API_BASE = import.meta.env.VITE_API_BASE_URL;
const questions = [
  {
    id: "social_preference",
    text: "Do you prefer being around others or alone?",
    options: ["Big Group", "Small Group", "Alone"],
  },
  {
    id: "energy_time",
    text: "What time of day do you feel most energetic?",
    options: ["Morning", "Afternoon", "Night"],
  },
  {
    id: "activity",
    text: "Pick a favorite activity:",
    options: ["Exploring", "Sleeping", "Swimming", "Hunting"],
  },
  {
    id: "pace",
    text: "What’s your pace in life?",
    options: ["Fast", "Medium", "Slow"],
  },
  {
    id: "stress_response",
    text: "How do you handle stress?",
    options: ["Calm", "Anxious", "Aggressive"],
  },
  {
    id: "favorite_color",
    text: "Pick a favorite color:",
    options: ["Blue", "Red", "Green", "Black", "White"],
  },
];

const currentQuestionIndex = ref(0);
const answers = reactive({});

function nextQuestion() {
  if (currentQuestionIndex.value < questions.length - 1) {
    currentQuestionIndex.value++;
  } else {
    submitAnswers();
  }
}

function prevQuestion() {
  if (currentQuestionIndex.value > 0) {
    currentQuestionIndex.value--;
  }
}
function handleAnswer(option) {
  answers[questions[currentQuestionIndex.value].id] = option;
  nextQuestion();
}
async function submitAnswers() {
  try {
    const response = await axios.post(`${API_BASE}/predict`, answers);
    const predicted = response.data.predicted_animal;
    router.push({ name: "Results", query: { animal: predicted } });
  } catch (error) {
    console.error("Failed to submit answers", error);
  }
}
</script>


<style scoped>
.quiz-container {
  max-width: 400px;
  margin: auto;
  font-family: Arial, sans-serif;
}
.buttons {
  margin-top: 1rem;
  display: flex;
  justify-content: space-between;
}
button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
.button-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
@media (max-width: 600px) {
  .button-container {
    flex-direction: column;
  }
}
</style>