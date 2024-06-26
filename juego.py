import pygame,random,objetos

proyectiles =[]

#juego corriendo
def jugando():
    juego = True
    while juego:
        
        try:
        #pantalla-------------------------------------------------------------------------------------------------------------------------------
            
            objetos.pantalla.blit(objetos.escala,(0,0))
            
            teclas= pygame.key.get_pressed()

            for estrellas in objetos.estrellas_lista:
                estrellas.generar()
                estrellas.movimiento()

            #jugador-----------------------
            objetos.jugador.generar()
            objetos.jugador.teclado(teclas)
            objetos.jugador.colision_pant()
            #------------------------------    
            objetos.asteroide.generar()
            for asteroides in objetos.asteroide_sprite:
                asteroides.movimiento()

            
            for proyectil in proyectiles:
                proyectil.generar()
                proyectil.disparar()
        #pantalla--------------------------------------------------------------------------------------------------------------------------------
        #colisiones------------------------------------------------------------------------------------------------------------------------------
                for asteroide in objetos.asteroide_sprite:
        
                    if asteroide.rect.colliderect(proyectil.generar()):
                        asteroide.rect.x = 900
                        asteroide.rect.y = random.randint(0,500)
                        objetos.puntaje += 1
                        if objetos.puntaje % 5 == 0:
                            for asteroide in objetos.asteroide_sprite:
                                asteroide.velx += 1
                            
                        proyectiles.remove(proyectil)
            if pygame.sprite.spritecollide(objetos.jugador,objetos.asteroide_sprite,False):
                perdida = True
        #colisiones--------------------------------------------------------------------------------------------------------------------------------

        #perdiste----------------------------------------------------------------------------------------------------------------------------------
                
                if perdida == True:
                    while perdida:
                        
                        objetos.pantalla.fill((0,0,0))
                        objetos.pantalla.blit(objetos.perdiste_texto,(395,250))
                        objetos.pantalla.blit(objetos.texto.render(f'tu puntuacion fue: {objetos.puntaje}',1,objetos.blanco),(350,300))
                        objetos.pantalla.blit(objetos.urban,(800,400))
                        teclas = pygame.key.get_pressed()
                        pygame.display.flip()
                        for evento in pygame.event.get():
                            if evento.type == pygame.QUIT:
                                    pygame.quit()

                        if teclas[pygame.K_SPACE]:
                            objetos.puntaje = 0
                            for asteroide in objetos.asteroide_sprite:
                                asteroide.velx = 3
                            objetos.jugador.rect.x= 0
                            objetos.jugador.rect.y = 0
                            for asteroide in objetos.asteroide_sprite:
                                if asteroide.rect.x < 500:
                                    asteroide.rect.x = random.randint(499,899)
                            jugando()
        #perdiste----------------------------------------------------------------------------------------------------------------------------------
        #eventos-----------------------------------------------------------------------------------------------------------------------------------
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
    
                if pygame.KEYUP: 
                    if teclas[pygame.K_e] and objetos.jugador.recarga > 0:
                    
                        proyectil = objetos.Proyectil()
                        proyectiles.append(proyectil)

                        objetos.jugador.recarga -= 1

                    if teclas[pygame.K_r]:
                        objetos.jugador.recarga = 5
                    if  teclas[pygame.K_e] and teclas[pygame.K_r]:
                        objetos.jugador.recarga= 0
                    
        #eventos-----------------------------------------------------------------------------------------------------------------------------------
            recarga_text = objetos.texto.render(f'disparos {objetos.jugador.recarga}',1,objetos.rojo)
            aviso = objetos.texto.render(f'E para disparar, R para recargar',1,objetos.rojo)
            puntuacion = objetos.texto.render(f'puntaje:{objetos.puntaje}',1,objetos.blanco)
            objetos.pantalla.blit(recarga_text,(390,0))
            objetos.pantalla.blit(aviso,(390,20))
            objetos.pantalla.blit(puntuacion,(0,450))
            objetos.reloj.tick(30)  
            pygame.display.flip()    
        except pygame.error:
            pass
        except ValueError:
            pass
        

    
jugando()
