<script setup lang="ts">
import { ref, onMounted } from 'vue';
import * as d3 from 'd3'

let data = ref((function initData() {
  let d = []
  for (let i = 0; i < 200; i++) {
    for (let j = 0; j < 200; j++) {
      d.push(Math.floor(Math.random() * 4) - 1)
    }
  }
  return d
})())



function draw() {
  const svg = d3.select("#cell2")
    .append("svg")
    .attr("width", 800)
    .attr("height", 800);

  var colorScale = d3.scaleOrdinal()
    .domain([-1, 0, 1, 2])
    .range(["red", "none", "lightgreen", "darkgreen"]);

  var rectSize = 4; // 每个矩形的大小
  svg.selectAll("rect")
    .data(data.value)
    .enter()
    .append("rect")
    .attr("x", function (d, i) {
      return (i % 200) * rectSize;
    })
    .attr("y", function (d, i) { return Math.floor(i / 200) * rectSize; })
    .attr("width", rectSize)
    .attr("height", rectSize)
    .attr("fill", function (d) { return colorScale(d); });
}

function next() {
  let 
}

onMounted(() => {
  draw()
});

</script>

<template>
  <div class="matrix">
    <div id="cell2"></div>
    <button class="btn">next</button>
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
