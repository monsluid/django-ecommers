const app = Vue.createApp({
	delimiters:['{$','$}'],
	data(){
		return {
			cart:[],
			product:{},
			quantity:1,
			message: ""
		}
	},

	methods:{
		async getProduct(){
			const url = '/product' + location.pathname
			const { data } = await axios.get(url)
			this.product = data
		},
		
		incrementQuantity(){
			if(this.quantity >= this.product.stock){
				return
			}

			this.quantity++
		},

		decreaseQuantity(){
			if(this.quantity <= 1){
			this.showAlert('Debe selecionar al menos 1 producto')
				return
			}

			this.quantity--
		},

		showAlert(message){
			this.message = message

			setTimeout(() => this.message = "", 3000)
		},


		getSavedCart(){
			let savedCart

			if(localStorage.getItem('cart') === null){
				
				savedCart = []

			} else{
				savedCart = JSON.parse(localStorage.getItem('cart'))
			}
			return savedCart
		},

		addProduct(){
			 const productToCart = {
				 product_id: this.product.idProduct,
				 name: this.product.name,
				 quantity: this.quantity,
				 price: this.product.price,
				 total: this.quantity * this.product.price
			 }

			const product = this.cart.find( prod => prod.product_id === productToCart.product_id )

			if(!product){
				this.cart.push(productToCart)
			} else {
				product.quantity += productToCart.quantity
			}

			localStorage.setItem('cart', JSON.stringify(this.cart))


		},
	},


	created(){
		this.getProduct()
		this.cart = this.getSavedCart()
	}
});
app.mount('#vue-app');
