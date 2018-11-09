/*-- componente telefono --
  Este componente genera un modal con informacion pasada como parametros por medio
  de SLOTS. El modal contiene un boton que redirige al usuario a la url de redireccion
  pasada como propiedad 
*/
const modalInfo=  {
    props:['url_redirect'],
    data () {
      return {
      }
    },
    methods:{
        redirectToPage(){
            if(this.url_redirect != ""){
                location.href= this.url_redirect;
            }
            else{
                this.$parent.showModal=false;
            }
        }
    },
    mounted () {
    },
    template:/*html*/`
    <!-- template for the modal component -->
    <div id="modal-template">
        <transition name="modal">
            <div class="modal-mask">
            <div class="modal-wrapper">
                <div class="modal-container">

                <div class="modal-header">
                    <slot name="header">
                    default header
                    </slot>
                </div>

                <div class="modal-body">
                    <slot name="body">
                    </slot>
                </div>

                <div class="modal-footer">
                    <button class="modal-default-button btn btn-primary btn-sm" @click="redirectToPage">
                        Aceptar
                    </button>
                </div>
                </div>
            </div>
            </div>
        </transition>
    </div>
    `
  }
  
  /* Variable contenedora de la instancia del componente telefono*/
  var contenedorModalInfo = new Vue({
  el: '#componente_modal_info',
  data: {
    showModal: true
  },
  components:{
    'modal-info':modalInfo
  }
})