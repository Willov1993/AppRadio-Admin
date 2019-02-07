const modalTabla = {
    data(){
        return {
        }
    },
    methods: {
        aceptar(){
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
                            <table id="table_frecuencias" class="table table-striped table-bordered dt-body-center">
                                <thead>
                                    <tr>
                                        <th>Frecuencia</th>
                                        <th>Dia</th>
                                        <th>Hora Inicio</th>
                                        <th>Hora Fin</th>
                                    </tr>
                                </thead>
                            </table>
                        </div>
                        <div class="modal-footer">
                            <button class="modal-dafault-button btn btn-primary btn-sm" @click="aceptar">
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

var contenedorTable = new Vue({
    el: '#componente_table',
    data: {
        showModal: false,
        id: null,
    },
    components: {
        'modal-mostrar': modalTabla
    }
})