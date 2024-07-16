<template>
    <!-- <div id="cell2" class="w-full h-full"></div> -->
    <!-- <div id="cell2"></div> -->
    <svg width="300" height="300" background-color="red"></svg>
    <!-- <el-button type="primary" @click="nextStep">Primary</el-button> -->
</template>

<script setup lang="ts">
// import { ref, onMounted } from 'vue';
// import * as d3 from 'd3'
// import { normalDistribution } from '~/lib/utils'
// import { useData } from '~/stores/data'

// let svg
// let colorScale = d3.scaleOrdinal()
//     .domain([-1, 0, 1, 2])
//     .range(['#FA7070', "#FEFDED", "#C6EBC5", "#2C7865"]);
// let data = useData()
// console.log(data.initData)
// var rectSize = 8; // 每个矩形的大小

// function nextStep() {
//     data = useData()
//     console.log(data.initData)
//     svg.selectAll("rect")
//         .data(data.initData)
//         .attr("x", function (d, i) { return (i % 20) * rectSize; })
//         .attr("y", function (d, i) { return Math.floor(i / 20) * rectSize; })
//         .attr("width", rectSize)
//         .attr("height", rectSize)
//         .attr("fill", function (d) { return colorScale(d); })
//     console.log(123)
// }

// onMounted(() => {
//     console.log(1)
//     svg = d3.select("#cell2")
//         .append("svg")
//         .attr("width", 300)
//         .attr("height", 300)


//     svg.selectAll("rect")
//         .data(data.initData)
//         .enter()
//         .append("rect")
//         .attr("x", function (d, i) { return (i % 20) * rectSize; })
//         .attr("y", function (d, i) { return Math.floor(i / 20) * rectSize; })
//         .attr("width", rectSize)
//         .attr("height", rectSize)
//         .attr("fill", function (d) { return colorScale(d); });
// })

</script>

<style scoped></style>