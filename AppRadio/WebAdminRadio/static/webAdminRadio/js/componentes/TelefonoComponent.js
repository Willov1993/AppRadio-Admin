
/*-- componente telefono --
  este componente crea el elemento html para el input de telefonos, con los botones
  de agregar y eliminar, los cuales al ser presionados generaran mas inputs o eliminaran los
  existentes, ademas de que se puede acceder a toda la data de los inputs desde su atributo telefonos
*/
const Telefono=  {
  props:['telefono'],
  data () {
    return {
      telefonos:[],

    }
  },
  methods:{
    agregarRegistro(){
      this.telefonos.push({'nro_telefono': null})
    },
    eliminarRegistro(indice){
      this.telefonos.splice(indice,1)
    }
  },
  mounted () {
    this.agregarRegistro()
  },
  template:/*html*/`
  <div>
    <div v-for="(tel,index) in telefonos" v-bind:key="index" class="form-row">
      <div class="form-group col-md-4">
          <input v-model="tel.nro_telefono" v-bind:name="'telefono'" required maxlength="10" type="tel" class="form-control" placeholder="Ingrese el numero de telefono">
      </div>
      <div v-if="index != 0" class="form-group col-md-2">
          <button type="button" class="btn btn-primary" @click="eliminarRegistro(index)" >Eliminar</button>
      </div>
      <div class="form-group col-md-2">
          <button v-if="index == telefonos.length - 1" type="button" class="btn btn-primary" @click="agregarRegistro" >Agregar Nuevo</button>
      </div>
    </div>
  </div>
  `
}

/* Variable contenedora de la instancia del componente telefono*/
var contenedorTelefonos = new Vue({
  el: '#componente_telefono',
  components: {
    'telf' : Telefono
  },
  data:{
    bar: "foo"
  },
})

//contenedorTelefonos.$children[0].$data.telefonos -> para obtener la data!!