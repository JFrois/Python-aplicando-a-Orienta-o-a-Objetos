from Modelos.Restaurantes import Restaurante

restaurante_pizza = Restaurante(f"Pizza", "Pizzaria", "80406087000130", "121234431256789")
restaurante_dondo = Restaurante("Dondó", "Comida nordestina", "82173441000150", "119080706058")
restaurante_japones = Restaurante("Japonês do amor", "Japonesa", "42468159000185", "1190909005438")

restaurante_dondo.receber_avaliacao("Juan Frois", 5)

restaurante_dondo.receber_avaliacao("Roberto", 2)
restaurante_dondo.receber_avaliacao("Pedro Firmino", 1)



restaurante_japones.alterar_status()

def main():
    Restaurante.listagem_restaurantes()


if __name__ == '__main__':
    main()