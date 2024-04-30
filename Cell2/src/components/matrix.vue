<script setup lang="ts">
import { ref, onMounted, nextTick } from 'vue';
import * as d3 from 'd3'

let data = ref(new Array(40000).fill(0))
let step = ref(1)

function init() {
  let set = new Set()
  while (set.size != 400) {
    const i = Math.floor(Math.random() * 40000);
    set.add(i)
  }
  set.forEach(a => {
    data.value[a] = -1
  })
  data.value[Math.floor(Math.random() * 40000)] = 1
}

function draw() {
  const svg = d3.select("#cell2")
    .append("svg")
    .attr("width", 800)
    .attr("height", 800);

  var colorScale = d3.scaleOrdinal()
    .domain([-1, 0, 1, 2])
    .range(['#FA7070', "#FEFDED", "#C6EBC5", "#2C7865"]);

  var rectSize = 4; // 每个矩形的大小
  svg.selectAll("rect")
    .data(data.value)
    .enter()
    .append("rect")
    .attr("x", function (d, i) { return (i % 200) * rectSize; })
    .attr("y", function (d, i) { return Math.floor(i / 200) * rectSize; })
    .attr("width", rectSize)
    .attr("height", rectSize)
    .attr("fill", function (d) { return colorScale(d); });
}

// 获取正态分布的随机值
function nD(mean, standardDeviation) {
  let u = 0, v = 0;
  while (u === 0) u = Math.random(); // 确保 u 不为 0
  while (v === 0) v = Math.random(); // 确保 v 不为 0

  const z = Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
  return z * standardDeviation + mean;
}

function next() {
  // 上下左右
  let dir1 = [-1, 1, -200, 200]
  let dir2 = [-201, -199, 199, 201]
  const copy = new Array(...data.value)
  function rule(arr) {
    for (let i = 0; i < arr.length; i++) {
      if(data.value[i] === -1) arr[i] = -1
      else if(data.value[i] === 1) arr[i] = 2
      else if(data.value[i] === 2) arr[i] = 2
      else if(data.value[i] === 0) {
        let change = 0
        for (let j = 0; j < dir1.length; j++) {
          let pos = i + dir1[j]
          let p2 = 1
          if (pos >= 0 && pos < 40000) {
            if (data.value[pos] === 1) {
              let p1 = nD(0.8, 0.1) 
              if (p1 * p2 < 0.6) {
                change = change === 1 ? 1 : -1
              } else {
                change = 1
              }
            }
          }
        }
        for (let j = 0; j < dir2.length; j++) {
          let pos = i + dir2[j]
          let p2 = Math.sqrt(2) / 2
          if (pos >= 0 && pos < 40000) {
            if (data.value[pos] === 1) {
              let p1 = nD(0.7, 0.1)
              if (p1 * p2 < 0.6) {
                change = change === 1 ? 1 : -1
              } else {
                change = 1
              }
            }
          }
        }
        arr[i] = change
      }
    }
  }
  rule(copy)
  copy.forEach((x, i) => {
    data.value[i] = copy[i]
  })
  console.log(data.value)
}

function nextStep() {
  for (let i = 0; i < step.value; i++) {
    next()
  }
  draw()
}

onMounted(() => {
  init()
  draw()
});

</script>

<template>
  <div class="matrix">
    <div id="cell2"></div>
    <input type="text" v-model="step" placeholder=step />
    <button class="btn" @click="nextStep">next {{ step }} step</button>
  </div>
</template>

<style scoped>
.btn {
  margin: 10px;
  background-color: bisque;
}

.matrix {
  width: 100%;
  height: 100%;
  display: center;
}
</style>
