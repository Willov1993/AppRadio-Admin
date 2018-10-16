const Segmento = {
    data() {
        return{
            segmentos:[],
        }
    },
    methods: {
        agregarSegmento(){
            this.segmentos.push({'value': null})
        },
        eliminarSegmento(indice){
            this.segmentos.splice(indice, 1)
        }
    },
    mounted(){
        this.agregarSegmento()
    },
    template:/*html*/`
    <div>
        <div v-for="(segmento, index) in segmentos" v-bind:key="index" class="form-row">
            <div class="form-group col-md-2">
                <select disabled id="segmentoSelect" v-bind:name="segmento" class="custom-select form-control">
                    <option disable selected value="">--</option>
                </select>
            </div>
            <div v-if="index != 0" class="form-group col-md-2">
                <button type="button" class="btn btn-primary" @click="eliminarSegmento(index)">Eliminar</button>
            </div>
            <div class="form-group col-md-2">
                <button disabled id="btn_agregar" v-if="index == segmentos.length - 1" type="button" class="btn btn-primary" @click="agregarSegmento">Agregar otro segmento</button>
            </div>
        </div>
    </div>
    `
}

var contenedorSegmentos = new Vue({
    el: '#componente_segmento',
    components: {
        'segmento': Segmento
    }
})