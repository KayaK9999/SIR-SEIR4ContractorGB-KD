<template>
    <div class="h-full w-full flex flex-col">
        <div class="top">
            <div class="flex-1">
                <svg height="300" width="300"></svg>
            </div>
            <div class="flex-1 border-l"></div>
        </div>
        <div class="bottom"></div>
    </div>
</template>

<script setup lang="ts">

</script>

<style scoped>
.top{
    flex: 3 1 auto;
    display: flex;
    flex-direction: row;
    border: 1 solid red
}

.bottom {
    flex: 2 1 auto; 
    border: 1 'solid' 'red'
}
</style>