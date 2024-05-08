import {createApp} from "vue";
import {createRouter, createWebHistory} from "vue-router";
import {createHead} from "@vueuse/head";
import VuePapaParse from "vue-papa-parse";
import App from "./App.vue";
import routes from "./pages/urls.js";
import store from "./store/";
import utils from "./scripts/utils.js";

const app = createApp(App);

// 全局导入了所有的Vue文件，避免以后的依次导入
// import.meta.glob是一个函数，它接受一个glob模式作为参数，用于匹配文件路径。
// "./components/**/*.vue"是一个glob模式，它匹配./components/目录及其所有子目录中的所有.vue文件。
// { eager: true }是一个选项对象，当eager设置为true时，它会在初始加载时立即导入所有匹配的模块，而不是在运行时动态导入。
const widgets = import.meta.glob("./components/**/*.vue", { eager: true });
for (const path in widgets) {
    let componentConfig = widgets[path];
    const componentName = componentConfig.default.name;
    console.log('componentName: ', componentName)
    app.component(componentName, componentConfig.default || componentConfig);
}

app.mixin({
    methods: utils.filters,
});

const layouts = import.meta.glob("./layouts/**/*.vue", { eager: true });
for (const path in layouts) {
    let componentConfig = layouts[path];
    const componentName = componentConfig.default.name;
    app.component(componentName, componentConfig.default || componentConfig);
}

let mode = import.meta.env.VITE_STAGE;

let allRoutes = [...routes];

store.dispatch("setMode", mode);

let router = createRouter({
    history: createWebHistory(),
    base: import.meta.env.BASE_URL,
    routes: allRoutes,
});

// @vueuse/head是一个Vue的组合API，用于管理你的文档头部
// 帮助管理<title>、<meta>以及其他在文档头部的元素
const head = createHead();

app.use(VuePapaParse);

app.use(store);
app.use(router);
app.use(head);
app.mount("#app");
