
package listasimples;


public class Lista {
   
   int valores[];
   private int tamanho;

    //construtor
    public Lista(int tam){
        if (tam > 0) {
            tamanho = tam;
            valores = new int[tamanho];
        }
    }
    
    public int insere(int valor, int pos){
        if (pos >= 0 && pos < valores.length) {
            valores[pos] = valor;
            return valor;
        }
        return -1;
       
    }
    
    public int remove(int pos){
        int valor;
        if (pos >= 0 && pos < valores.length) {
            valor = valores[pos];
            valores[pos] = 0;
            return  valor;
        }
        return -1;
    }
   
   
}
