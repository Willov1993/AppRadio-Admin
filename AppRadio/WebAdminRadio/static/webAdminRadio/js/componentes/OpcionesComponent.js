/* -- Componente para opeciones --
    Este componente permite agregar varias opciones a una pregunta
*/

const Opcion = {
    data() {
        return {
            opciones[]
        }
    },
    methods: {
        agregarOpcion() {
            this.opciones.push({
                'descripcion': null
            })
        },
        eliminarOpcion(indice) {
            this.opciones.splice(indice, 1)
        }
    },
    mounted() {
        this.agregarOpcion()
    },
    template: /*html*/`
    <div>
        <div v-for="(pregunta, index) in opciones" v-bind:key="index" class="form-row">
            <div class="form-group col-md-10">
                <input required v-bind:name="'respuesta' + index" id="optInput" type="text" class="form-control" placeholder="Opcion" maxlength=150>
            </div>
        </div>
        <div class="form-group col-md-2" id="btn-eliminar-div">
            <div id="btn-eliminar">
                <button v-if="index != 0" type="button" class="btn btn-primary" id="addOpcion" @click="eliminarOpcion">Eliminar</button>
            </div>
        </div>
        <button type="button" class="btn btn-primary" id="addOpcion" @click="agregarOpcion">Agregar otra opción</button>
    </div>
    `
}

var contenedorOpcion = new Vue({
    el: '#componente_opcion',
    components: {
        'opcion': Opcion
    }
})