
const RedSocial=  {
    data () {
      return {
        redes_sociales:[],
      }
    },
    methods:{
      agregarRegistro(){
        this.redes_sociales.push({'nombre': null,'link': null, esOtra:false})
      },
      eliminarRegistro(indice){
        this.redes_sociales.splice(indice,1)
      },
      verificarOtraRed(e,indice){
        this.redes_sociales[indice].nombre= e.target.value
        this.redes_sociales[indice].esOtra= (this.redes_sociales[indice].nombre == "Otra")
      }
    },
    mounted () {
      this.agregarRegistro()
    },
    template:/*html*/`
    <div>
      <div v-for="(red,index) in redes_sociales" v-bind:key="index" class="form-row">
        <div class="form-group col-md-4">
            <input v-model="red.link" v-bind:name="'red_social_url'" type="url" class="form-control" placeholder="Ingrese la url de la red social">
        </div>
        <div class="form-group col-md-2">
            <select @change="verificarOtraRed($event,index)" v-bind:name="'red_social_nombre'" class="custom-select form-control">
                <!--option disabled selected value="">Red Social</option-->
                <option value="Facebook">Facebook</option>
                <option value="Twitter">Twitter</option>
                <option value="Youtube">Youtube</option>
                <option value="Otra">Otra</option>
            </select>
        </div>
        <div v-if="red.esOtra == true" class="form-group col-md-2">
            <input v-model="red.nombre" class="form-control" v-bind:name="'red_social_nombre'" placeholder="Ingrese el nombre de la red social">
        </div>
        <div v-if="index != 0" class="form-group col-md-2">
            <button type="button" class="btn btn-primary" @click="eliminarRegistro(index)" >Eliminar</button>
        </div>
        <div class="form-group col-md-2">
            <button v-if="index == redes_sociales.length - 1" type="button" class="btn btn-primary" @click="agregarRegistro" >Agregar Nuevo</button>
        </div>
      </div>
    </div>
    `
  }

  /* Variable contenedora de la instancia del componente telefono*/
  var contenedorRedesSociales = new Vue({
    el: '#componente_redsocial',
    components: {
      'redsocial' : RedSocial
    }
  })