
Vue.component('name-list', {

    props: ['list'],

    template: `
                <div class="content">
                    <label class="label"> Names: </label>
                    <ul>
                        <task v-for="name in list" v-text="name"></task>
                    </ul>
                </div>
            `

});

Vue.component('task', {

    template: `
                <li><slot></slot></li>
            `

});

new Vue({

    el: '#root',

    data: {
        newName: '',
        nameList: []
    },

    methods: {
        addName(){
            this.nameList = this.nameList.concat(this.newName);
            this.newName = '';

            Vue.http.post('/api/name', {foo: 'this.newName'}).then((response) => {
                console.log(foo);
            });
        }
    },

    mounted(){
        this.$http.get('/api/name').then((response) => {
            this.nameList= this.nameList.concat(JSON.parse(response.body));
            console.log(this.nameList);
        });
    }


});