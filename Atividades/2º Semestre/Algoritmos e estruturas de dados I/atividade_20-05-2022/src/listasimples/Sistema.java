/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package listasimples;

/**
 * =
 * @author DELL
 */
public class Sistema {

    public static void main(String[] args) {
       Lista lista = new Lista(5);
       lista.insere(10, 0);
       lista.insere(20, 1);
       lista.insere(30, 2);
       System.out.println(lista.valores[0]);
       System.out.println(lista.valores[2]);
       lista.remove(0);
       System.out.println(lista.valores[0]);
       System.out.println(lista.valores[1]);
       System.out.println(lista.valores[2]);
    }
    
}
