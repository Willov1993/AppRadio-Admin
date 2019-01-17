/* -- Componente Preguntas -- 
    Este componente crea las preguntas para el concurso
*/
//import OpcionesComponente from './OpcionesComponent.js'

const Pregunta = {
    /*components: {
        'option': OpcionesComponente
    },*/
    data() {
        return{
           preguntas:[]
        }
    },
    methods: {
        agregarPregunta(){
            this.preguntas.push({
                'descripcion': null
            })
        },
        eliminarPregunta(indice){
            this.preguntas.splice(indice, 1)
        }
    },
    mounted(){
        this.agregarPregunta()
    },
    template:/*html*/`
    <div>
        <div v-for="(pregunta, index) in preguntas" v-bind:key="index" class="form-row">
            <div class="form-group col-md-10">
                <label for="preguntaInput">Pregunta:</label>
                <input required v-bind:name="'pregunta' + index" id="preguntaInput" type="text" class="form-control" placeholder="Ingrese pregunta" maxlength=150>
            </div>
            <div class="form-group col-md-10">
                <label for="respuestaInput">Respuesta:</label>
                <input required v-bind:name="'respuesta' + index" id="respuestaInput" type="text" class="form-control" placeholder="Opcion" maxlength=150>
            </div>
            <div class="form-group col-md-2" id="btn-eliminar-div">
                <div id="btn-eliminar">
                    <button v-if="index != 0" type="button" class="btn btn-primary" id="addHorario" @click="eliminarPregunta">Eliminar</button>
                </div>
            </div>
        </div>
        <button type="button" class="btn btn-primary" id="addPregunta" @click="agregarPregunta">Agregar otra pregunta</button>
    </div>
    `
}

/* Variable contenedora de la instancia del componente horario */
var contenedorPregunta = new Vue({
    el: '#componente_pregunta',
    components: {
        'pregunta': Pregunta
    }
})

