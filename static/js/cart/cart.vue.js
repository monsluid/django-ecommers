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
		async incrementQuantity(id){
			// busca el producto en el carrito
			const product = this.cart.find(prod => prod.product_id == id)
			// obtenemos el stock desde la api
			const { data } = await this.getCurrentStock(id)
			// validamos
			if(product.quantity >= data.stock){
				this.popoverMessage(id)
				return
			}
			// si tenemos disponibles sumamos
			product.quantity += 1
			// calculamos el total
			product.total = product.quantity * product.price
			//
			localStorage.setItem('cart', JSON.stringify(this.cart))

		},

		decreaseQuantity(id){
			// busca el producto en el carrito
			const product = this.cart.find(prod => prod.product_id == id)

			if(product.quantity <= 1){
				return
			}

			product.quantity--
			product.total = product.quantity * product.price
			localStorage.setItem('cart', JSON.stringify(this.cart))
		},

		deleteProduct(id){
			const cart = this.cart.filter(product => product.product_id != id)
			this.cart = cart
			localStorage.setItem('cart', JSON.stringify(this.cart))
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

		async getCurrentStock(id){

			const url = '/product/api/product/' + id

			try {
				return await axios.get(url)
			} catch(error) {
				console.error(error)
			}

		},

		popoverMessage(id){
			$(`#${id}`).popover('show')

			setTimeout(() => $('.btn-popover').popover('hide') , 2000)
			
		},

	},


	computed:{
		setTotal(){
			return this.cart.reduce((total, producto)=> total + producto.total,0)
		}
	},

	created(){
		this.cart = this.getSavedCart()
	}
});
app.mount('#vue-app');
