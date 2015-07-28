################
### Цепочка преивентов, делающая доступным газетное дело и использование Гермионы в нем. ###                
################

label newsp_pre_letter: #Приходит письмо из министерства магии о газете.

    call bigletter(["{size=-7}От: Министерства Магии\nКому: Профессору Альбусу Дамблдору\n\n{/size}"
    "{size=-4}Дорогой профессор Дамблдор.\n\nМы хотим сообщить Вам, что Сообщество Магов в целом (в лице Министерства Магии) "
    "и попечительский совет Хогвартса в частности хотели бы, чтобы ваша Школа организовала свой печатный орган.\n\n"
    "В связи с Вашим вызывающим уважение мастерством документооборота мы считаем, что Вас не затруднит "
    "Организовать в Хогвартсе небольшую редакцию и приступить к изданию стенгазеты.\n\n"
    "Т.к. данное поручение связано с новыми стандартами образования учеников и было "
    "инициировано во имя высших ценностей, мы будем следить за популярностью данного издания в Школе "
    "и выплачивать соответствующую компенсацию за ваши усилия и для поддержания журналистской деятельности.\n\n{/size}",
    "{size=-4}Вы можете распоряжаться данными фондами по своему усмотрению.\n\nТакже мы понимаем, что освоение такого "
    "необычного для традиционной Школы Волшебников рода деятельности требует немалых усилий, "
    "выбор сотрудников редакции из числа учеников и преподавателей остается на ваше усмотрение.\n\n{/size}"
    "{size=-3}С уважением,\nМинистерство Магии.{/size}"])

    $ nsp_pre_letter = 2

    $hero(m, "Во имя Великого Песчаного Кактуса!..")
    $hero("Я должен выжать из этой возможности все что можно. Фонды, значит...")
    $hero("Нужно обязательно расспросить дружище Северуса об этом.")
    $hero("Но делиться галлеонами - это не по мне.")
    $hero("Думаю, однако, что привлечь Гермиону к написанию статей будет нелишне.")
    $hero("Но сначала придется разобраться, что к чему. Да, нужно поговорить со Снейпом !")

    call screen main_menu_01

label newsp_pre_snape_dialog:

    $screens.Hide("snape_main")
    $snape.State("door").Visibility("body")

    if nsp_pre_snape == 4:
        $hero(m,"Здравствуй, Северус !")
        $hero("И все-таки я не знаю, с чего начать. Вообще ничего в голову не приходит.")
        $snape("~29//Хорошо, тогда сделаем так. Где-то на столе, среди бумаг, было приложение к каталогу Дахры.")
        $snape("~29//Там был целый раздел товаров для книгопечатания, наверное, и для газет что-то найдется..")
        $snape("~29//Посмотри повнимательнее и закажи себе самоучитель редактора.")
        $snape("~28//Надеюсь этого хва... а... а... атит. Чуть челюсть не вывихнул. Все, до первого выпуска больше никаких вопросов.")
        $hero("{size=-5}Похоже нужно браться за дело и поскорее.")
        $ nsp_pre_snape = 5

    if nsp_pre_snape == 3:
        $hero(m,"Здравствуй, Северус !",
        "Как по твоему, я смогу делать газету в одиночку ?")
        $snape("~29//Далась тебе эта газета. Давай я лучше расскажу, сколько очков и за что я дал недавно одной маленькой шлю... то есть ученице.")
        $hero("Пожалуйста, не отвлекайся, для меня это важно !")
        $snape("~29//Ну ладно, ладно. Ты же пишешь свои дурацкие отчеты ? Ну и газету сделать сможешь.")
        $snape("~29//Укажи внизу мелким шрифтом, что в редакции четыре анонимных студента, чтобы списать все промахи на них. А сам будь как бы ни при чём.")
        $snape("~05//Только помни, что чем меньше людей тебя тут видят, тем меньше шанс раскрыться. Не стоит приглашать к себе посторонних.")
        $hero("Минутку ! Если я буду делать всё сам, не выходя из кабинета, то как же газета окажется на стене главного холла ?")
        $snape("~29//Хм. Да нет ничего проще. У Альбуса на столе есть магическая печать. С ее помощью любой проштампованный лист попадает прямо на стенд.")
        $snape("~29//Так что с этим проблем не предвидится.")
        $snape("~06//Пожалуй на этом все, твои распросы пора уже патентовать как снотворное зелье.")
        $ nsp_pre_snape = 4

    if nsp_pre_snape == 2:
        $hero(m,"Здравствуй, Северус !",
        "Итак, как выглядит стенгазета ?")
        $snape("~29//Ох...")
        $snape("~29//Ну представь себе лист 4 метра в длину и 3 в высоту, висящий на стене.")
        $snape("~29//На этом листе написан текст в 8 колонок, кроме того сверху в центре можно разместить особо важный материал.")
        $snape("~29//Если ты будешь заниматься газетой сам, то текст придется придумать, по сути для этого годится материал отчетов.")
        $snape("~29//В хорошей газете на первой странице живые фотографии знаменитостей или интересных событий. Но их тебе взять неоткуда.")
        $snape("~06//Если честно, эта тема вгоняет в сон, пожалуй мне лучше сейчас уйти, можем продолжить в другой раз.")
        $ nsp_pre_snape = 3
    
    if nsp_pre_snape == 0 or nsp_pre_snape == 1:

        if nsp_pre_snape == 0:
            $hero(m,"#(Так, нужно начать издалека, чтобы он не догадался о моих фон... в смысле проблемах.)")
            $hero("Здорово, Северус, как жизнь ?")
            $snape("~01//А какая по-твоему, какой может быть жизнь у такого темного мага, как я ?")
            $hero("Эм-кхм. Ну я даже не знаю... Зловещей ?")
            $snape("~11//Зловещей ? Почему это ? Вовсе нет. Я дам еще одну подсказку.")
            $snape("~29//У черного-черного мага, который знает себе цену, жизнь какая ?")
            $hero("У черного-черного мага ? Наверное, жизнь - тоска и боль ?")
            $snape("~07//Да с какой это стати ! Что за глупости ! Я совсем не о том.")
            $snape("~24//Итак, последняя попытка.")  
            $snape("~29//У мага, который всегда в безупречно черном модном костюме, жизнь всегда полна...")
            $hero("#(Блин, я уже почти забыл, зачем его позвал. Нужно как-то поделикатнее сменить тему.)")
            $hero("У черного мага в костюме жизнь должна быть полна ГАЗЕТ !")
            $snape("~29//Вообще-то ПОКЛОННИЦ ! Какие еще газеты ? При чем тут газеты ?")
            $hero("Ну вот я тут сижу, сижу... Заняться почти нечем. Дай, думаю, газету почитаю. Так нету ее")
            $snape("~24//Так закажи себе газет, в чем проблема то ? Сразу узнаешь, что в нашем мире делается.")
            $snape("~24//Эти ничтожные репортеришки столько врут про всяких других ничтожеств, что только успевай читать.")
            $hero("Ну лично меня интересуют местные дела, а не мировые. А своих газет у Хогвартса нет.")
            $hero("Хоть свою редакцию открывай... А кстати, это идея ! Что скажешь ? Дашь пару советов ?")
            $ nsp_pre_snape = 1
        else:
            $hero(m,"Привет, Северус !")
            $hero("Меня не покидает желание открыть свою газетную редакцию. Подскажешь, что к чему ?")

        if snape_friendship > 40:
            $snape("~29//Лучше бы ты пошел и спросил кого-нибудь, кто хоть немного больше меня интересуется печатным словом")
            $hero("Хорошо, не вопрос. Тогда на повестке дня другой важный вопрос")
            $snape("~28//Вот, другое дело !")
            $hero("Итак, у меня появились идеи, как нам более равномерно поделить внимание девушек Слизерина между собой...")
            $snape("~11//Я тут кое-что вспомнил... В детстве у меня была вторая по важности мечта - издавать свою газету.")
            $snape("Прости, а какая же тогда была первая ?")
            $snape("~13//Убить всех надоедливых смеющихся ребятишек. МУ-ХА-ХА.")
            $snape("~24//Ладно, у меня есть еще дела, но следующий раз я отвечу на твои вопросы.")
            $ nsp_pre_snape = 2
        else:
            $snape("~29//Джинни, есть всего две вещи в мире, которые интересуют меня меньше газет.")
            $snape("~29//Но говорить о них мне хочется еще меньше, чем о газетах. Есть намного более приятные занятия.")
            $snape("~01//Кстати о приятных занятиях. Мне уже пора.")
            $hero("#(Нет, так дело не пойдет, нужно сначала сильнее расположить Снейпа к себе.)")

    jump snape_nothing_exit

label newsp_pre_snape_dialog2:

    $screens.Hide("snape_main")
    $snape.State("door").Visibility("body")

    $hero("Привет, Северус, как дела ?")
    $snape("~02//Пока не родила.")
    $hero(g4,"ЧТО ? Ты уже трахал своих студенток без предохранения ?")
    $snape("~01//И незачем так кричать, разве ты не знал эту бородатую шутку ?")
    $hero(m,"Ладно, проехали. У меня тут есть серьезная проблема из-за этих проклятых модеров.")
    dr "О нет. Очень прошу, придерживайся уже наконец сценария ! А то я, пожалуй, сделаю мод со сменой пола главного героя."
    $hero(g5,"Пощады ! Я все понял.")
    $snape("~26//Опять он говорит сам с собой ...")
    $hero(m,"Итак, я сделал свой первый газетный выпуск. Но у него крайне низкая популярность. Может быть есть идеи, как поправить положение ?")
    $snape("~05//Снова эта газета... Ладно, слушай внимательно.")
    $snape("~06//Популярность газеты зависит от интересности материала и качества его оформления. Тут нужны навыки писателя и оформителя, а также соответствующие инструменты.")
    $snape("~06//Кроме того, было бы неплохо приобрести фотоаппарат и научиться им пользоваться. А еще, стоит поохотиться за каким-нибудь особо интересным материалом.")
    $snape("~06//Он может значительно повысить интерес учеников.")
    $hero("И какой же материал ты имеешь ввиду ? Я же сижу взаперти ! Неужели делу поможет фотография шкафа ?")
    $snape("~26//Ну лично я предложил бы побольше секса ! Это именно то, что интересует подростковую аудиторию.")
    $hero("Но Северус, ведь учителя тоже это увидят !")
    $snape("~06//Так ведь ты не от своего имени издаешь, а от анонимной редакции. Никто не узнает, что газета связана с тобой.")
    $snape("~02//А еще у меня появилась идея, кто именно сможет добыть для тебя сюжеты.")
    $hero(g9,"Да, у меня тоже есть на примете одна девочка.")
    $snape("~02//Удачи, дружище.")

    $ nsp_newspaper_menu = 4

   

    jump snape_nothing_exit

label nsp_hermione_pre1 :

    if nsp_newspaper_menu == 4:
        m "Здравствуй, дит... хм... Гермиона."
        $herView.hideshowQQ( "body_02.png", pos )
        her "Профессор ?"
        her "Что-то не так, сэр ?"
        m "Да что-то я задумался глядя на тебя. Ведь ты уже совсем взрослая."
        $herView.hideshowQQ( "body_24.png", pos )
        her "Вы меня смущаете..."
        her "У вас на уме еще какое-то странное задание ?"
        m "Вовсе нет. Есть тут одна проблема, которой я могу поделиться только с достойным доверия человеком."
        $herView.hideshowQQ( "body_13.png", pos )
        her "Это как-то связано с соревнованием факультетов ? Может быть, вы хотите провести проверку правомочности начисления очков Слизерину ?"
        m "А-кха-кхм. Кхм-кхе-кхе."
        $herView.hideshowQQ( "body_01.png", pos )
        her "Что с вами, сэр ? Вам плохо ? Принести воды ?"
        m "Кхм-кха. Нет, все в порядке. Просто ты не совсем угадала. Даже не знаю, стоит ли говорить..."
        ">Вы задумчиво хмуритесь, в то время, как Гермиона сгорает от любопытства."
        $herView.hideshowQQ( "body_11.png", pos )
        her "Но сэр ! Разве я когда-нибудь вас подводила ? "
        her "Вы же сами мне всегда помогаете с очками факультету. Позвольте и мне помочь !"
        m "(Приготовься, Джинни, сейчас тебе предстоит повесить ей на уши целый котел лапши)"
        m "Ну хорошо, слушай внимательно. Речь действительно идет о соревновании, но ..."
        $herView.hideshowQQ( "body_05.png", pos )
        her "Я так и знала, сэр ! Какие-то шлю..., то есть ученицы, опять добывают очки нечестным способом, не так ли ?"
        her "Кто на этот раз ? Когтевранки или пуффендуйки ? Как же я не люблю этих хитрых нахалок, норовящих всё выставить напоказ перед учителями !"
        m "Мда..."
        $herView.hideshowQQ( "body_24.png", pos )
        her "Ой, простите, сэр. Но с вами совсем другое дело. Ведь я вовсе не добиваюсь нечестного преимущества, а только восстанавливаю справедливость !"
        $herView.hideshowQQ( "body_01.png", pos )
        m "Это хорошо, но речь вовсе не о соревновании между факультетами."
        m "Все намного серьезнее. Дело в том, что министерство хочет выяснить, в какой школе самые активные, объективные, умные и самодеятельные ученики."
        m "Для этого директорам поручено организовать школьную стенгазету."
        her "Стенгазету ?"
        m "Да, и оценивать ее будет само министерство. Сейчас у меня осталась одна вакансия - ведущий журналист, и я просто ума не приложу, кого взять на эту роль."
        ">Гермиона задумчиво смотрит на вас. Внезапно ее лицо озаряется пониманием."
        $herView.hideshowQQ( "body_10.png", pos )
        her "Вы могли бы предложить эту роль самой активной, самой начитанной ученице - то есть мне !"
        m "Наверное можно попробовать. Если ты готова делать всё необходимое для поддержания чести школы..."
        m "Хотя, с другой стороны, ты, возможно, слишком скромна, чтобы желать разде... в смысле увидеть свое имя на золотой доске почета в главном зале."
        $herView.hideshowQQ( "body_04.png", pos )
        her "Но сэр, именно золотая дос..., то есть поддержание чести школы и есть моя главная цель тут, в Хогвартсе !"
        ">Гермиона мечтательно закатывает глаза"
            
    if nsp_newspaper_menu == 5 :
        m "Здравствуй, Гермиона"
        m "Что ты думаешь по поводу позиции ведущего журналиста в стенгазете ?"
       
    if hermi.whoring >= 12 and touched_by_boy == True and lock_public_favors == False : 
        $herView.hideshowQQ( "body_11.png", pos )
        her "Сэр, примите меня в вашу редакцию, вы не пожалеете ! Скажу без ложной скромности, что никто в школе не составляет текст домашних заданий быстрее."
        m "(О да, детка !)"
        m "Ну что же, думаю можно попробовать. В следующий раз мы обсудим возможные темы для публикации."
        her "Спасибо, сэр !"
        $ nsp_newspaper_menu = 6
            
    else :
        $herView.hideshowQQ( "body_16.png", pos )
        her "Я хотела бы уточнить, что от меня потребуется. Надеюсь, мне не придется делать ничего неприличного перед всей школой ?"
        m "(Кажется она пока недостаточно сговорчива. Придется получше обработать эту девку перед следующим разговором.)"
        m "Пока у меня нет конкретных идей, думаю я вызову тебя позже."
        $ nsp_newspaper_menu = 5
    
    hide screen bld1
    $herView.hideQ()
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 

    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
        
    ### MUSIC BLOCK ###
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    ### END OF BLOCK ###
  
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

label nsp_snape_dialog3 :

    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ menu_x = 0.2 #Menu is moved to the left side. (Default menu_x = 0.5)
    $ tt_xpos=350 #Defines position of the Snape's full length sprite.
    $ tt_ypos=0
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    show screen snape_02 #Snape stands still.
    show screen bld1
    show screen snape_main
    with Dissolve(.3)
    $screens.Hide("snape_main")
    $snape.State("door").Visibility("body")
    
    $hero (g9, "Привет, Северус. Зачем пожаловал ?")
    $snape("~02//{size=+2}Ха-ха-ха.{/size}")
    $hero (m, "Что ?")
    $snape ("~28//{size=+5}Му-ха-ха-ха-ха !{/size}")
    $hero ("Похоже ты чем-то очень доволен ?")
    $snape ("~02//И он еще спрашивает... Ну ты шутник.")
    $hero ("Ничего не понимаю.")
    $hero ("Минутку... Ага!")
    $hero ("Тебе так сильно понравился последний выпуск газеты ?")
    $snape ("~02//Не то слово ! Непристойные фото этой маленькой шлюхи прямо на стенде !")
    $snape ("~02//Прямо в главном зале !")
    $snape ("~02//Да я не променял бы это дажде на секс с тре... нет с двумя лучшими моими ученицами!")
    $hero (g9,"Я так понимаю, теперь тебе уже не скучно говорить про газету ?")
    $snape ("~09//Да, пожалуй я был не прав. Издавать {size=+3}такую{/size} газету - было отличной идеей.")
    $snape ("~06//И я кое-что тебе принес.")
    $hero (m,"Вот как ?")
    $snape ("~01//Да. Это хрустальный шар, который я нашел среди своего ненужного хлама.")
    $snape ("~01//Когда-то один древний маг пытался сделать или найти артефакт, который мог бы показывать людей или предметы на расстоянии.")
    $snape ("~01//В итоге он объявился с этим хрустальным шаром. Вроде бы ему удавалось частично достичь нужного эффекта, хотя точной информации уже не осталось.")
    $snape ("~01//Так или иначе, в ходе экспериментов шар треснул и перестал работать. Восстановить его пока что никому не удавалось.")
    $snape ("~04//Я подумал, что если не помогает магия волшебников, идеи могут быть у тебя.")
    $snape ("~10//С работающим шаром твои возможности по сбору материалов могли бы значительно вырасти.")
    $snape ("~28//Раздевалки девочек, их спальни, всевозможные маленькие секреты...")
    $snape ("~02//Ты просто {size=+4}обязан{/size} его починить !.")
    $hero (m,"Да, пожалуй оно стоит того !")    
    
    $ nsp_newspaper_menu = 9
    
    jump snape_nothing_exit

label nsp_hermione_train :

    if nsp_newspaper_menu == 15 :
        $ nsp_newspaper_menu = 16
        
        $herView.hideshowQQ( "body_01.png", pos )
        her "Здравствуйте, профессор."
        $herView.hideshowQQ( "body_13.png", pos )        
        her "А что это у вас в руках ? Похоже на хрустальный шар."
        her "Неужели вы хотите позаниматься со мною прорицаниями ?"
        m "Я хочу позаниматься с тобой грязным се... Кхм. Новым заклинанием."
        m "Оно позволит улучшить материалы, получаемые в ходе репортажа и поможет нашей газете."
        $herView.hideshowQQ( "body_06.png", pos )  
        her "Мне уже не терпится..."
        $herView.hideshowQQ( "body_35.png", pos )
        m "(Эх, что она со мной делает.)"
        $herView.hideshowQQ( "body_01.png", pos )        
        ">Прошло два часа."
        m "Итак, все готово. Я скоро вызову тебя для дополнительных тренировок."
        her "Да, сэр."
        $ nsp_genie_sphere_level_exp += 1
        call nsp_genie_sphere_level_check
        
    else :
    
        m "Итак, девочка, мы должны установить связь в пределах комнаты."
        $herView.hideshowQQ( "body_122.png", pos )
        her "Всегда готова к связям с вами, сэр !"
        "Прошло 2 часа, ваше владение хрустальным шаром улучшилось."
        $ nsp_genie_sphere_level_exp += 1
        call nsp_genie_sphere_level_check
        
    ">Опыт владения шаром [nsp_genie_sphere_level].[nsp_genie_sphere_level_exp]."

    hide screen bld1
    $herView.hideQ()
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 

    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
        
    ### MUSIC BLOCK ###
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    ### END OF BLOCK ###
   
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

label nsp_her_demo :

    dev "Приветствую вас, игрок."
    dev "К сожалению, в рамках эвентов газеты данное событие дальше не сделано."
    dev "Ждите продолжения в следующих версиях."

    if nsp_event_rights_1 >= 1 and nsp_event_magls_1 >= 1 and nsp_event_kviddich_1 >= 1 and nsp_event_forest_1 >= 1 and nsp_event_studio_1 >= 1 :
        call nsp_her_demo2
    
    jump nsp_newsp_themes

label nsp_her_demo2 :

    dev "Вам удалось открыть все эвенты газеты, готовые в данной версии игры."
    dev "Но не расстраивайтесь, в будущем добавится еще много интересного !"
    dev "А если хотите стимулировать меня и других разработчиков работать быстрее, то :"
    dev "1) Оставьте отзыв на {a=http://wtrus.ixbb.ru/viewtopic.php?id=9}ФОРУМЕ{/a}"
    dev "2) Принимайте активное участие в обсуждениях на {a=http://wtrus.ixbb.ru/viewtopic.php?id=9}ФОРУМЕ{/a}"
    dev "3) Создавайте свой контент для игры."
    dev "4) ....."
    dev "5) PROFIT"
    dev "P.S. А еще у вас есть беспрецедентная возможность повлиять на дальнейшее развитие игры. "
    dev "Для этого нужно принять участие в {a=http://wtrus.ixbb.ru/viewtopic.php?id=74}голосовании{/a}."
    dev "До новых встреч."
    
    return

