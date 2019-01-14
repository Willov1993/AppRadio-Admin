/* -- Componente Horarios -- 
    Este componente crea los elemetos de día para agregar más días a los horarios
    de los segmentos
*/

const Premio = {
    data() {
        return{
           premios:[]
        }
    },
    methods: {
        agregarPremio(){
            this.premios.push({
                'descripcion': null
            })
        },
        eliminarDia(indice){
            this.premios.splice(indice, 1)
        }
    },
    mounted(){
        this.agregarPremio()
    },
    template:/*html*/`
    <div>
        <div v-for="(premio, index) in premios" v-bind:key="index" class="form-row">
            <div class="form-group col-lg-4">
            <p style="white-space: pre-line;">{{ premio.descripcion }}</p>
            <textarea id="desc" style="width:100%" v-model="premio.descripcion" placeholder="Ingrese cada premio en una línea"></textarea>
            </div>
        </div>
    </div>
    `
}

/* Variable contenedora de la instancia del componente horario */
var contenedorPremio = new Vue({
    el: '#componente_premio',
    components: {
        'premio': Premio
    }
})

