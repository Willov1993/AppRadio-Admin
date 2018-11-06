const modalLocutor = {
    data(){
        return {
        }
    },
    methods: {
        redirectToPage(){
            location.href = this.$parent.getURL;
        },
        cancelar(){
            this.$parent.showModal = false;
        }
    },
    template: /*html*/`
    <!-- template para el componente de locutor -->
    <div id="modal-template">
        <transition name="modal">
            <div class="modal-mask">
                <div class="modal-wrapper">
                    <div class="modal-container">
                        
                        <div class="modal-header">
                            <slot name="header">default header</slot>
                        </div>

                        <div class="modal-body">
                            <slot name="body"></slot>
                        </div>

                        <div class="modal-footer">
                            <button class="modal-default-button btn btn-primary btn-sm" @click="redirectToPage">
                                Sí, estoy seguro
                            </button>
                            <button class="modal-default-button btn btn-primary btn-sm" @click="cancelar">
                                Cancelar
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </transition>
    </div>
    `
}

var contenedorLocutor = new Vue({
    el: '#componente_locutor',
    data: {
        showModal: false,
        id_locutor: null,
        id_segmento: null,
    },
    components: {
        'modal-locutor': modalLocutor
    },
    computed: {
        getURL(){
            return '/webadmin/locutores/asignar/' + this.$data.id_locutor + '/segmento/' + this.$data.id_segmento
        }
    }
})