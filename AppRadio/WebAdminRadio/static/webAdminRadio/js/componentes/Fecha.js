/* -- Componente Horarios -- 
    Este componente crea los elemetos de día para agregar más días a los horarios
    de los segmentos
*/

const Horario = {
    data() {
        return{
            horarios:[]
        }
    },
    methods: {
        agregarDia(){
            this.horarios.push({
                'fecha_inicio': null,
                'fecha_fin': null,
            })
        },
        eliminarDia(indice){
            this.horarios.splice(indice, 1)
        }
    },
    mounted(){
        this.agregarDia()
    },
    template:/*html*/`
    <div>
        <div v-for="(horario, index) in horarios" v-bind:key="index" class="form-row">
            <div class="form-group col-md-3">
                <label>Fecha inicio</label>
                <input v-model="horario.fecha_inicio" type= "date" name="tipo" id="fecha_incioInput" class="custom-select form-control" required>
            </div>
            <div class="form-group col-md-3">
                <label>Fecha fin</label>
                <input v-model="horario.hora_inicio" name="hora_inicio" type="date" class="form-control" required>
            </div>
        </div>
    </div>
    `
}

/* Variable contenedora de la instancia del componente horario */
var contenedorHorario = new Vue({
    el: '#componente_horario',
    components: {
        'horario': Horario
    }
})

