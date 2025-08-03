<template>
  <div class="result-page max-w-md mx-auto text-center">
    <div v-if="animal" class="card p-4 shadow">
      <h2 class="text-3xl font-bold mb-4">Your Spirit Animal</h2>
      <img
        :src="imageSrc"
        :alt="animal"
        class="mx-auto w-54 h-54 object-contain mb-4"
      />
      <div>
        <h2 class="text-2xl font-semibold capitalize mb-2 text-red">
          {{ animal }}
        </h2>
        <p class="mb-4">{{ description }}</p>
        <button
          @click="retry"
          class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
        >
          Try Again
        </button>
      </div>
    </div>

    <div v-else class="text-red-500">
      <p>No spirit animal found. Go back and take the quiz.</p>
      <router-link to="/" class="text-blue-600 underline"
        >Start Over</router-link
      >
    </div>
  </div>
</template>

<script setup>
import { computed } from "vue";
import { useRoute, useRouter } from "vue-router";

const route = useRoute();
const router = useRouter();

const animal = route.query.animal || "";

const info = {
  dog: {
    desc: "Loyal, friendly, and social. You thrive in companionship.",
    img: "/animals/dog.png",
    backColor: "brown",
  },
  cat: {
    desc: "Independent and curious. You value your space and observe quietly.",
    img: "/animals/cat.png",
    backColor: "white",
  },
  dolphin: {
    desc: "Playful and intelligent. You adapt easily and love connection.",
    img: "/animals/dolphin.png",
    backColor: "cyan",
  },
  owl: {
    desc: "Wise and observant. You think deeply and prefer calm nights.",
    img: "/animals/owl.png",
    backColor: "gray",
  },
  lion: {
    desc: "Bold and proud. You lead with confidence and presence.",
    img: "/animals/lion.png",
    backColor: "yellow",
  },
  rabbit: {
    desc: "Gentle and quick. You’re sensitive but resourceful.",
    img: "/animals/rabbit.png",
    backColor: "pink",
  },
  bear: {
    desc: "Strong and protective. You value peace but stand firm when needed.",
    img: "/animals/bear.png",
    backColor: "brown",
  },
  fox: {
    desc: "Clever and agile. You find creative ways to solve problems.",
    img: "/animals/fox.png",
    backColor: "orange",
  },
};
const key = (animal || "").toString().toLowerCase();
const description = computed(
  () => info[key]?.desc ?? "An interesting spirit animal!"
);
const imageSrc = computed(() => info[key]?.img ?? "/animals/default.png");
const ShadowColor = computed(() => info[key]?.backColor ?? "#cd4713");
function retry() {
  router.push({ name: "Home" });
}
</script>

<style scoped>
.result-page {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI",
    sans-serif;
}
</style>
