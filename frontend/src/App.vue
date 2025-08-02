<script setup>
</script>

<template>
  <div style="height: 100%; display: flex; flex-direction: column">
    <img
      src="../logo/logo.svg"
      alt="Spirit Animal"
      class="mx-auto mt-50 mb-5"
      style="width: 400px"
    />
    <router-view />
    <div
      style="color: white; margin: auto auto 0 auto"
      class="github-link mt-auto"
    >
      <a href="https://github.com/manuallymz">2025 © Nima Ramezani </a>
    </div>
  </div>
</template>

<style scoped>
</style>
