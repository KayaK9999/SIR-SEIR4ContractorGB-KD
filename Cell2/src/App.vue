<script setup lang="ts">
import matrix from './components/matrix.vue'
</script>

<template>
  <div class="two-column-layout">
    <div class="left-column">
      <matrix />
    </div>
    <div class="right-column">
      <!-- 右侧内容 -->
    </div>
  </div>
</template>

<style scoped>
.two-column-layout {
  display: flex;
  flex-direction: row;
  width: 100vw;
  height: 100vh;
}

.left-column {
  flex: auto;
  /* 左侧栏样式 */
}

.right-column {
  border-left: 1px saddlebrown solid;
  flex: 0 0 500px;
  /* 右侧栏样式 */
}
</style>
