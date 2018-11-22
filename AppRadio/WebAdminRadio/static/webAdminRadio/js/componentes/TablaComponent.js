const modalBorrar = {
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
    <!-- tempalte para el componente de borrar -->
    <div id="modal-tempalte">
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
                        <div class="table-container">
                            <table id="data_table" class="table table-striped table-bordered dt-body-center">
                                <thead>
                                    <tr>
                                        <th>ID</th>
                                        <th>Imagen</th>
                                        <th>Titulo</th>
                                        <th>Cliente</th>
                                        <th>Emisora</th>
                                        <th>Frecuencias</th>
                                        <th>Acciones</th>
                                    </tr>
                                </thead>
                                <tbody>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </transition>
    </div>
    `
}

var contenedorBorrar = new Vue({
    el: '#componente_borrar',
    data: {
        showModal: false,
        id: null,
        objects_to_delete: null, 
    },
    components: {
        'modal-borrar': modalBorrar
    },
    computed:{
        getURL(){
            return '/webadmin/' + this.$data.objects_to_delete + '/' + this.$data.id + '/eliminar'
        }
    }
})