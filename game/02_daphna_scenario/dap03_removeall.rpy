﻿#########################
########### LEVEL 03 ########
#########################
##### REQUEST_03 Remove All #####
#########################
label dap_request_03: #LV.3 (Whoring = 7 - 15)
    
    $music("Daphne Theme")

if IsRunNumber(1):
    if daphne.whoring < 6:
        $hero("Полагаю, что она еще не готова...// Может позже....")
        call daphne_main_menu_requests
    else:
        $daphne("~73 01 1 smi")
        "> Вы замечаете, что Дафна впервые за все время, излучает море позитива"
    $hero("Эмоции вас словно переполняют....")
    $daphne("~55 c0 1 gri// Да, профессор...//~32 c0 1 smi// Вы правы....")
    $hero("Позвольте спросить мисс Гринграсс, \"что\" так сильно подняло вам настроение?")
    $daphne("Конечно, сэр...//~55 n2 2 smi// Если вам интересно, я расскажу....")
    $hero("#(Черт...)// #(Она чертовски хороша когда улыбается...)")
    $hero(g9, "#(Кажется моё настроение тоже поднимается....)")
    $daphne("~37 02 2 ope")
    menu:
        "\"Подрочить под столом\"":

            hide screen blktone
            with d3
            "> Вы опускаете руки под стол, и обхватываете свой член..."
            hide screen blktone8
            with d3
            hide screen genie
            show screen genie_jerking_off
            with d3
            pause
            show screen genie_jerking_off

            $hero(m, "#(О, да...)")
            $hero(g9, "#(Меня заводит её болтовня...)")
            $daphne("~70 00 3 dis// ....Профессор?// Что вы.....?")
            $hero(m, "Чешу ногу мисс Гринграсс.... Если вам так интересно....// Продолжайте... я весь во внимании....")
            $daphne("~37 02 2 neu// Эм...  ...Хорошо, сэр.")
            $hero(g9, "#(Какие же вы все наивные....)")
            $daphne("~37 02 2 ope// Ну... после этого, все стали считать меня своей конкуренткой...//~37 03 1 neu// Но я то знаю, что мне не будет равных в этом конкурсе...")
            $hero(m, "#(Давай девочка, смотри на меня...)// #(О, да... как это круто...)")
            $daphne("~46 00 1 neu// А грязнокровка Грейнджер... это совсем другая тема...//~73 01 1 pur// Вы не подумайте, сэр... мне нет дела до её мнения...//~55 03 2 neu// Но.....//~55 03 3 dis// #(Черт... что он там делает?)")
            $hero("#(Не нравится мне её взгляд...)")
            $daphne("~46 00 2 dis// ...Профессор, вы могли бы прекратить это делать?")
            $hero(g4, "Агрx....// #(Да чтоб вас обеих....)")
            $daphne("Профессор?!")
            $hero(m, "Гхм... Конечно...")

            show screen genie
            with d3
            pass

            $hero("Продолжайте мисс Гринграсс....")
            $daphne("~73 01 1 pur// Эм... Сэр...// ...Вы же не из-за рассказов меня сюда позвали?")
        "\"Выслушать её\"":
            $hero(m, "#(Думаю стоит послушать...)")
            $daphne("~73 01 1 neu// В общем.... Кто-то узнал про то, что вы тренируете меня....// Стали расспускать грязные слухи, о том как я «получила» это место....//~55 03 1 neu// Что бы они не говорили у меня за спиной, я не обращаю на это внимание...")
            $hero("Это верный поступок....")
            $daphne("Спасибо, сэр....//~73 01 1 ehh// Не знаю почему, но после этого, все кто тоже участвует в конкурсе, стали считать меня своей первой конкуренткой...")
            $hero("Вам бы многие позавидовали Дафна...// Они понимают, что быть заявленной на мисс Хогвартс директором - это большое преимущество....")
            $daphne("~62 03 1 pos// И даже оно мне не нужно....// Ведь я то знаю, что мне не будет равных в этом конкурсе...")
            $hero("Несомненно, вы правы....")
            $daphne("~46 00 1 neu// А грязнокровка Грейнджер... это совсем другая тема...// Вы не подумайте, сэр... мне нет дела до её мнения...// Но.....")
            $hero("«Но»... что?")
            $daphne("~46 c0 1 neu// Но, сэр.... вы же меня ради этой болтовни позвали?")

    $hero("Верно...// Эм... Что на счет вашей популярности мисс Гринграсс?")
    $daphne("~73 01 2 ehh// ....Популярности?//~36 00 2 pou// Сэр, вы же знаете... мне нет дела до мнения недоволшебников...")
    $hero("Не заставляйте меня снова вам объяснять, почему это так важно....")
    $daphne("~64 00 1 neu// Не нужно профессор, я поняла....// Мне снова нужно что-то сделать?")
    $hero("Да....// У меня есть для вас новое задание мисс Гринграсс...// Я надеюсь вы справитесь....")
    $daphne("Я постараюсь, профессор...")
    $hero("Для начала, я хочу посмотреть на ваше нижнее белье...")
    $daphne("~73 02 1 ehh// ...Сново, сэр?")
    $hero("Да...")
    $daphne("~47 02 1 pri")
    "> Дафна уверено раздевается...."

    $screens.Show(Dissolve(1), "blkfade")
    $daphne.ItemsCustomize(update={"combi:daphne_combi_handsonhip"}).chibi.State(appearance="g").Refresh()
    $daphne.ItemsCustomize(update={"skirt:daphne_skirt"})
    pause.5
    $screens.Hide(Dissolve(1), "blkfade") 
    $screens.Show("ctc").Pause().Hide("ctc")

    $hero("Гхм......// А теперь, девушка...// Вы должны отправится в таком виде на занятия....")
    $daphne("Э-э-э....//~99 03 1 pri// Профессор... я не смогу....")
    $hero("Почему?// ....Вы же не стесняетесь меня?")
    $daphne("~99 s3 2 ang// Это разные вещи, сэр...//~33 01 1 ang// Перед вами....// То есть вы....")
    $hero("Ничем не отличаюсь от других мисс Гринграсс...// К тому же, я уже говорил вам, что ваша победа зависит от того какое вы окажете впечатление на сокурсников...")
    $hero("Я же не могу придумать некое правило, запрещающее голосовать за других студенток....")
    $daphne("~36 00 1 pou// Я понимаю...// Хотя....//~24 c0 1 ehh// А если нам \"что-то такое\", придумать....//~55 02 2 ehh// Вместе...// Что скажете, сэр?")
    $hero("........?!")
    $hero("(Не понял?!)")
    $daphne("~64 01 1 neu// Так что, профессор?//~55 00 1 smi// Я могу сделать \"что-то другое\" для вас?")
    $hero(g9, "#(«Что-то другое?»)")
    menu:
        "\"Ах ты маленькая извращенка...\"":
            $hero("Да, кажется я понял {b}что{/b} ты можешь сделать....")
            $daphne("~99 02 3 dis//{size=+7}ЧТО!?{/size}// {size=+7}Нет! Я не это имела ввиду...{/size}// {size=+7}Как вы вообще могли о таком подумать?{/size}")
            $hero(m, "Да расслабься, я пошутил....")
            $daphne("~77 02 3 dis// Это ни черта не смешно!")
            $hero("Согласен, это было глупо...// Проехали....")
            $daphne("~69 n2 2 dis// #(Черт.... что на {b}меня{/b} нашло?!)//~77 03 3 ang// (....Почему я вообще, это сказала?!)")
            $daphne.liking-=10
        "\"Странно это все....\"":
            $hero(m, "Что вы имеете ввиду?")
            $daphne("~36 00 1 pou// Ну... Может я помогу вам....// А вы поможете мне выиграть конкурс...")
            $hero("Я бы с радостью, но это будет как минимум некрасиво....// Да и не вы ли минуту назад утверждали, что вам не нужны никакие поблажки?")
            $daphne("...........//~36 02 1 neu// Эм.... вы правы...// Простите....")

    $hero("В общем...// Как видишь, других вариантов нет....// Благодаря этому, ты станешь еще на шаг ближе к победе...")
    $daphne("~55 02 2 pou//...Я не уверена, получится ли у меня?")
    $hero("Я верю что вы справитесь....")
    $daphne("~74 03 1 pou// Ну... Хорошо...// Я попробую....")
    $hero("Отлично мисс Гринграсс, жду вас вечером с отчетом....// Но прежде чем вы уйдете, у меня кое что есть для вас....")

elif IsRunNumber(2):
    if hero.Items.Count("mag3") == 0:
        "> Для продолжения данного ивента, вам необходим «Журнал для взрослых»"
        call daphne_main_menu_requests
    else:
        $hero("Хм... И так мисс...//Сегодня я хочу, чтобы вы произвели впечатление на учеников.")
        $daphne("Эм...//~26 s3 2 ope// Мне нужно сделать это снова?")
        $hero("Верно...// Я в вас не сомневаюсь мисс Гринграсс...")
        $daphne("~55 00 3 smi// Хорошо... я попробую, сэр...")
        $hero("Славно...// Жду вас вечером с отчетом...")

elif IsRunNumber(3):
    if hero.Items.Count("mag4") == 0:
            "> Для продолжения данного ивента, вам необходим «Порно журнал»"
            call daphne_main_menu_requests
    else:
        $hero("Хм... И так мисс...//Сегодня я хочу, чтобы вы произвели впечатление на учеников.")
        $daphne("Эм...//~26 s3 2 ope// Мне нужно сделать это снова?")
        $hero("Верно...// Я в вас не сомневаюсь мисс Гринграсс...")
        $daphne("~55 00 3 smi// Хорошо... я попробую, сэр...")
        $hero("Славно...// Жду вас вечером с отчетом...")

elif IsRunNumberOrMore(4):
    $hero("Хм... И так мисс...//Сегодня я хочу, чтобы вы произвели впечатление на учеников.")
    $daphne("Эм...//~26 s3 2 ope// Мне нужно сделать это снова?")
    $hero("Верно...// Я в вас не сомневаюсь мисс Гринграсс...")
    $daphne("~55 00 3 smi// Хорошо... я попробую, сэр...")
    $hero("Славно...// Жду вас вечером с отчетом...")

return


######################################################################################################
############################################## COMPLITE ##############################################
######################################################################################################


label dap_request_03_complete:
    $daphne.Visibility()
    $daphne.chibi.State("door", speed="go").Trans(d4, "blink").Trans("go center", "blink") # Если делать dissolve в движении, то сбивается счетчик времени. Лучше выполнить появление чибика стоя, затем уже двигать его 
    pause.5
    $screens.ShowD3("bld1")

    $daphne.State(pos="door").Visibility("body+")("~55 00 1 smi// Добрый вечер, профессор Дамблдор.")

    $music("Daphne Theme")

    if IsRunNumber(1):
        $hero("Добрый вечер Дафна...// Вы справились с заданием?")
        $daphne("Эм... да, сэр....")
        menu:
            "\"Расскажите по подробнее мисс Гринграсс\"":
                $daphne("~46 00 1 neu// Э-э... Сначала я думала что сгорю со стыда...// Но, когда я зашла на лекцию по защите от темных искувств...// Никто даже не обратил на меня {b}такого{/b} внимания...//~37 n0 1 pou// Как будто я....// Понимаете, сэр?// Ну... одеваюсь так каждый день...")
                $hero("#(Хм.....)// #(«Защита от темных искувств...»)// #(Эту дребедень у них вроде как Северус ведет...)")
                $hero(g9, "#(Он там наверное прихерел от такого...)")
                $daphne("~46 00 1 neu// ...Почему это так, профессор?")
                $hero(m, "Эм.... Ну я думаю, что он не ожидал от вас такого поступка, вот и все....// Впрочем я его понимаю....")
                $hero(g9, "Будь я на его месте, наверное, тоже бы охренел....")
                stop music 
                $daphne("~73 01 1 ang// {b}!!!!!!!!!!!!!!{/b}//~55 03 1 dis// Сэр... вы о чем?!// #(Он вообще, это {size=+3}мне{/size} говорит?)")
                $hero(g4, "............?!// #(Черт......)// #(Что она спросила?)")
                play music "music/Music for Manatees.mp3"
                $hero(m, "Эм.... Ну я спорил сам с собой?")
                $daphne("~26 00 2 smi// «С собой», профессор?!")
                $hero("Да... я нахожу это невероятно забавным....// Гхм... а в прочем мисс...// Кажется вы рассказывали мне доклад...")
                $daphne("~55 02 1 smi// Ах да... я продолжу сэр...")
            "\"Хорошо, можете быть свободны...\"":
                $daphne("...........//~74 00 2 pur// То есть, мне не нужно ничего рассказывать, сэр?")
                $hero("Только если вы находите необходимым, поделится этим со мной....")
                $daphne("~26 00 3 smi// Не то чтобы {b}необходимым{/b}....")
                $hero("Ну хорошо... Я понял...// Можете рассказать, я слушаю....")
                $daphne("~46 00 1 neu// Э-э... Сначала я думала что сгорю со стыда...// Но, когда я зашла на лекцию по защите от темных искувств...// Никто даже не обратил на меня {b}такого{/b} внимания...//~37 n0 1 pou// Как будто я....// Понимаете, сэр?// Ну... одеваюсь так каждый день...")
                $hero("#(Хм.....)// #(«Защита от темных искувств...»)// #(Эту дребедень у них вроде как Северус ведет...)")
                $hero(g9, "#(Он там наверное прихерел от такого...)")

        $daphne("~46 s1 1 ope// Эм... В общем профессор Северус....//~00 c1 1 smi// Ну.... от увиденного, он вошел в ступор, сэр...")
        $hero(g9, "#(Представляю его рожу...)")
        $daphne("~55 c2 1 gri// Все... как и я, жутко смеялись...")
        $hero(m, "#(Забавно...)// #(Она научилась видеть в этом, юмор...)")
        $daphne("~24 c0 1 pou// Единственное что я не поняла - это то... кто такой Джинни?")
        stop music 
        $ renpy.play('sounds/scratch.wav')
        $hero(g4, "......Что?!")
        $hero(m, "Он вам что-то рассказал про него?")
        $daphne("Оу... Нет...// Это были скорее мысли в слух...//~55 02 2 ehh// В конце занятия, он выпроводил меня к двери, и сказал что-то вроде: «Почему я отдал её Джинни? Может еще не поздно все исправить?»")
        play music "music/Music for Manatees.mp3"
        $hero("Гхм....// Видите ли мисс Гринграсс, профессор Северус, так же хотел заняться вашим обучением...// Но не надеялся, что вы сможете чего-то достичь...// И по этому, отправил вас ко мне...// А теперь как видите, спохватился...// Но вы не переживайте...// Я поговорю с ним, по этому поводу...")
        $daphne("~46 00 2 neu// Эм... Хорошо...// Ну дальше, в общем... я осталась в таком виде до конца занятий...//~28 c0 2 smi// И хоть все криво смотрели на меня, я старалась не обращать на них никакого внимания...")
        $hero("Это похвально Дафна....// Вы не перестаете меня удивлять...")
        $daphne("~74 c3 2 gri//Я стараюсь, профессор...")
        $daphne.whoring += 1
        $wtevent.Finalize("daphne_pre_menu")
    elif IsRunNumber(2):
            $hero("Добрый, Дафна...// Расскажешь как прошел сегодняшний день?")
            $daphne("Эм....// Ну....//~26 02 1 pri// Профессор, я....//~77 02 3 neu// В общем я не смогла сделать это...")
            $hero("Хм... Что же вас смутило в это раз, мисс?")
            $daphne("Сэр, когда я вам говорила, что не обращала внимания на реакцию других студентов...//~46 01 2 dis// Это была ложь....// Я не могу выбросить из головы это ужасное чувство стыда....// Которое поглощает меня целиком....//~66 s0 2 dis// И эти крики, тыканье пальцами, вроде «Посмотри, в чем она одета»....//~26 w3 3 dis// Я так не могу, профессор....// Не могу отбросить ту мысль, что мне еще раз придется все это испытать...")
            $hero("Хм... Я вижу, мисс, вы так и не поняли зачем я вас просил сделать это?// Ведь то, что вам становится стыдно, неловко в подобных ситуациях....// Совсем нормально...")
            $daphne("~55 s0 2 neu// Но, тогда зачем....")
            $hero("Да для того, чтобы вы смогли испытать, и побороть свои амбиции, мисс...// Неужели вы этого не понимаете?")
            $daphne("..........")
            $hero("Если вам будет наплевать на мнение окружающих....// То конкурс для вас будет легкой прогулкой по подиуму...")
            $daphne("~78 02 3 ang// ...Но, эти парни... они...")
            $hero("Что бы они не делали...// Единственный способ избавится от их насмешек - это демонстрировать что вам это нравится...")
            $daphne("~26 01 3 ang// Я не получаю от этого удовольствие...")
            $hero("Я и не прошу этого...// Сделайте вид, будто вам от этого становится хорошо...// Вот увидите, это несомненно сработает.")
            $daphne("~55 01 2 neu// ...Я не знаю, получится ли у меня...")
            $hero("Гхм....// Ладно, Дафна...// У нас еще есть время...// Я верю, что в следующий раз вы справитесь...")
            $daphne("~78 01 2 neu// ...Постараюсь, профессор.")
            $hero("А это, я думаю вам должно помочь...")
            $ renpy.play('sounds/win2.mp3')
            "> Вы даете Дафне «Журнал для взрослых»"
#            hero.Items.Count("mag3") -= 1
            $daphne("~78 02 3 dis// Это же журнал для взрослых, сэр!?")
            $hero("Именно.// Прочтите его на досуге...// Полагаю он вам поможет...")
            $daphne("~26 01 1 ope// Эм....//~55 02 2 smi//  Хорошо... Я возьму его...")
            $daphne.whoring += 1
            $wtevent.Finalize("daphne_pre_menu")
    elif IsRunNumber(3):
            $hero("Ну что, девушка...// Вы выполнили мое поручение?")
            $daphne("~26 01 2 smi// Да, сэр...// Выполнила...")
            $hero("Великолепно!// Что ж... может вы порадуете меня рассказом?")
            $daphne("Ах, да... Конечно...//~55 s2 2 ope//  Э-э... в общем...// ..........// Я прочитала в журнале, который вы мне дали...//~78 02 3 ope//  Как симулировать симпатию к эксгибиционизму...")
            $hero("Вы знаете, что значит это слово...?")
            $daphne("~55 00 2 smi// Теперь... да.")
            $hero("Ну, и что же...?")
            $daphne("~77 02 2 ope// Когда эти двое в очередной раз начали смеяться...//~26 w0 2 ehh//  Я просто хлопнула рукой себя по попе, и улыбнулась им...")
            $hero("И как они отреагировали?")
            $daphne("~44 w1 2 neu// .........//~44 01 1 smi//  Они смотрели на меня с открытым ртом когда уходила...// Да, ваш совет действительно был полезен...//~18 22 2 smi//  Это даже немного забавно, смотреть на их недоумение.")
            $hero("Славно мисс Гринграсс....// Я знал что вы оправдаете мои надежды.")
            $daphne("~78 00 2 smi// Спасибо, профессор...")
            $hero("Что ж, я думаю раз уж вы нашли для себя полезным мой подарок....// Тогда примите еще один...// Полагаю он так же откроет вам много нового.")
            $ renpy.play('sounds/win2.mp3')
            "> Вы даете Дафне «Порно журнал»"
#            hero.Items.Count("mag4") -= 1
            $daphne("~55 02 2 ope// Эм... Сэр, но это же...")
            $hero("Мисс, не сомневайтесь в моих действиях...// Просто полистайте в свободное время...")
            $daphne("~78 00 1 smi// Хорошо, профессор...")
            $daphne.whoring += 1
            $wtevent.Finalize("daphne_pre_menu")
    elif IsRunNumber(4):
        $hero("Здравствуйте, мисс...// Идут ли на пользу вам, наши занятия?")
        $daphne("~11 01 1 smi// Несомненно, профессор...")
        $hero("Приятно слышать это от вас, Дафна...// Ну... Возможно вы бы хотели...")
        $daphne("~11 w3 1 smi// Да, да... Я поняла, сэр...// Садитесь по удобнее.")
        $hero("Хорошо... Можешь начинать.")
        $daphne("~26 02 1 ope// Эм... Я, как вы и посоветовали, посмотрела журнал с....//~55 01 1 dis// В общем это... это так мерзко.// Мне не хотелось его дальше смотреть...//~77 01 1 smi// Но....// Ваши советы, профессор... они всегда были ценными, и....//~22 02 1 ehh// Понимала я их только тогда, когда уже было поздно...")
        $hero("Какой же вывод вы сделали, мисс Гринграсс?")
        $daphne("~77 01 2 ope// Э-э....//~26 01 1 neu// Что вы как бы то ни было, всегда оказываетесь правы, сэр...")
        $hero("#(Ммм... Хорошо...)")
        $daphne("Что нужно прислушиваться к вашим советам...")
        $hero("#(Да, да, отлично...)// И стало быть....")
        $daphne("~55 s1 1 smi// Слушаться вас, профессор.")
        $hero(g9, "#(Ну наконец-то)// Это похвально, мисс...// Я вновь рад тому, что вы поняли это сами.// Эм... А что касается моего задания? Оно выполнено?")
        $daphne("...Да, сэр.//~77 02 2 dis// Но... Я предпочла бы не вдаваться в подробности...// Я сделала что вы просили, а теперь можно я пойду?")
        menu:
            "- Расскажите мне, что случилось -":
                $hero(m, "Мисс... Почему мне нужно каждый раз напоминать вам, зачем мы это делаем...// Вы уже столько всего прошли... что мешает вам сейчас?")
                $daphne("........// Эм... Просто...//~26 01 2 dis// Тот парень....// Я никогда бы не стала....")
                $hero("Как же я смогу вам помочь разобраться, если вы молчите?")
            "- Да, конечно... -":
                $hero(m, "Хорошо можете идти...// Только не говорите мне потом, что нужно было слушаться меня...// Почему все именно так получилось...// Ступайте.")
                $daphne("...........//~55 01 3 dis// Не могу... Мне и в правду нужно разобраться в этом...")
                $hero("Ну так расскажите.// Расскажите мне по порядку, как и что случилось.")
                $daphne("............")

        $daphne("Ладно....// Эм... Я видела в том журнале что вы мне дали...//~26 01 2 dis// Как девушки заигрывали с парнями...// И я решила сделать так же...//~26 w2 2 ang// Просто попробовать...// Посмотреть парень себя поведет...//~55 s2 3 dis// Я не думала....")
        $hero("Расслабьтесь, мисс...// Давайте по порядку.")
        $daphne("~77 02 1 pri// Хорошо...// В общем я подошла к парню который сидел на скамейке в раздевалке...//~77 02 2 dis// И делала те штуки, которые.... из журнала...")
        $hero("Из журнала!?")
        $daphne("~26 02 2 dis// Да... Гладила его по... в...")
        $hero("Я понял, мисс....")
        $daphne("~55 w2 3 dis// Кажется ему были приятны...// Мои движения...")
        $hero("Вы это поняли!?")
        $daphne("~77 01 2 pri// Он тяжело дышал, и смотрел мне в глаза...// Я... я не знаю что произошло...//~77 02 2 dis// Я не заметила как он достал эту штуку....// Я не понимала что происходит...//~77 w3 3 dis// Она была... была огромная...// Он сказал, что бы я обхватила его...//~26 w0 2 dis// Гхм... Я хотела уйти... Но держал меня за руку, и тянул её туда...")
        $hero("Вы поддались?")
        $daphne("У меня не было выбора...// Он сильно схватил меня... и....//~77 02 3 ang// Я сделала ему рукой, что он просил...//~77 01 2 pri// И все...")
        $hero("Вам или ему это понравилось?")
        $daphne("Я не обращала на него внимания....// Если закрыть глаза, то в этом нет ничего такого...")
        $hero(g9, "#(Хе-хе, кроме члена в руке)")
        $daphne("~77 02 2 dis// Сэр, я сделала что вы просили... и, можно я....")
        $hero(m, "Да конечно, Дафна... Можете быть свободны.")
        $daphne.whoring += 1
        $wtevent.Finalize("daphne_pre_menu")
    elif IsRunNumber(5):
        $hero("#(На мой взгляд, в этой сфере Дафна уже в полне преуспела)")
        call daphne_main_menu_requests

    return