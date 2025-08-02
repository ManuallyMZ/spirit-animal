<template>
  <div class="result-page p-6 max-w-md mx-auto text-center card">
    <div class="mt-25">
      <p>Welcome to the Spirit Animal game!</p>
      <p>Answer some questions and i will guess your</p>
      <p><b>Spirit Animal</b></p>
    </div>
    <div class="mt-auto">
      <button @click="$router.push({ name: 'Quiz' })" class="mt-4">
        <p class="font-bold">Start Quiz</p>
      </button>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
/* body {
  background-color: rgb(215, 255, 255);
} */
</style>