const base = {
    get() {
        return {
            url : "http://localhost:8080/python1s2c1/",
            name: "python1s2c1",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "基于python 旅游网站"
        } 
    }
}
export default base
