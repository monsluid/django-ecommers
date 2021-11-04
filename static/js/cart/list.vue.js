// Vue App - carrito de Compras
// Daniel Monsrreal
// 20 Oct 2021

const app = Vue.createApp({
	delimiters:['{$','$}'],
	data() { 
		return {
			cart:[],
			products:[],
			query:''
		}
	},

	methods:{
		async getProducts(){
			const url = '/product/api/list'
			const { data } = await axios.get(url)
			this.products = data
		},

		async searchProduct(query){
			url = `/product/api/search?q=${query}`
			const { data } = await axios.get(url)
			this.products = data
		},

		productDetails(id){
			location.href = `/shop/product/${id}`
		}
	},
	
	
	created(){
		this.getProducts()
	},

	watch:{
		query(value,old){
			this.searchProduct(this.query)
		}
	}
});
app.mount('#vue-app')
