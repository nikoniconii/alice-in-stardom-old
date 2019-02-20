######################### What type of lunch is it?

label whatlunch:
    
    $ lunchtype = renpy.random.randint(1,4)
    
    if lunchtype == 1:
        
        jump normallunch
        
    if lunchtype == 2:
        
        jump ravenous
        
    if lunchtype == 3:
        
        jump leisurely
        
    if daytype == 4:
        
        jump busy
        
        
        



######################## Normal lunch

label normallunch:
    
    $ normallunch = renpy.random.randint(1)
    
    if normallunch == 1:
        
        scene dinnerday
        with fade
        
        show a smile
        with Dissolve(0.5)
        
        a "{i}It's lunch time again. Time to eat!{/i}"
        
        show t frowntalk at center
        show a smile at right
        show j smile at left
        with Dissolve(0.5)
        
        t "The food here is ridiculous. Can’t I just get a sandwich?"
        
        show t frown at center
        show j talk at left
        
        j "You can. There’s the black truffle lobster sandwich topped with gold flakes."
        
        show t frowntalk at center
        show j smile at left
        
        t "...Again, can't I just get a sandwich? Hello?"
        
        show t frown at center
        show a sing at right
        
        a "I suppose it does taste delicious."
        
        show a smile at right
        
        a "{i}I order the \"sandwich\", but request that they take out the gold flakes. It feels like such a waste if they just pass right through my intestines.{/i}"
        a "{i}I guess I shouldn't be thinking about that when I'm eating...{/i}"
        
        show j talk at left
        
        j "I'm done. What about you two?"
        
        show j smile at left
        show t frowntalk at center
        
        t "I’m in the process of dissecting my steak to make it more manageable for consumption."
        
        show t frown at center
        show a sing at right
        
        a "I’m almost done. There’s still much to do after all."
        
        show a smile at right
        
        a "{i}So what am I going to do for the afternoon?{/i}"
        
        #### call screen
        
        
        
        
        
label ravenous:
    
    $ ravenouslunch = renpy.random.randint(1,5)
    
    if ravenouslunch == 1:
        
        scene dinnerday
        with fade
        
        show a smile at right
        show l drool at left
        show c smile at center
        with Dissolve(0.5)
        
        a "{i}I'm absolutely famished! Good that I've made it here before starving to death!{/i}"
        
        l "Yur rudy fur fud too, Arisssssse?"
        
        show c shock at center
        
        c "Don't speak with your mouth full! It's hardly polite!"
        
        show a sing at right
        
        a "It’s okay. I don’t mind. I’m quite hungry myself, so I totally get it."
        
        show c smile at center
        show a smile at right
        
        a "{i}Lis struggles to swallow down her food, then gestures over to the plates in front of her.{/i}"
        
        l "Go ahead and have some of mine in the meantime! I ordered lots!"
        
        show c talk at center
        
        c "You always order so much. You won't be able to finish it."
        
        show c smile at center
        
        l "Who said I can't finish it? I have ten stomachs!"
        
        show c talk at center
        
        c "Nobody has ten stomachs!"
        
        show c smile at center
        
        l "Cows! Cows have multiple stomachs!"
        
        show c talk at center
        
        c "Even cows only have a single stomach. It’s just divided into four compartments. And you aren’t a cow, either!"
        
        show c smile at center
        
        a "{i}I hardly care if it's four stomachs or four compartments, but I'm eating till I fall!{/i}"
        
        l "Look at that spirit, Cherry! You should be more like Alice."
        
        show c talk at center
        
        c "It {i}is{/i} a feat of physics to pile so much food on a plate without it toppling over. This must be Alice’s Second Law of Food Towers."
        
        show c smile at center
        
        a "{i}I wonder if she'd ever tell me what is the first law.{/i}"
        
        scene dinnerday
        with fade
        
        show a frown at right
        show l smile at left
        show c shock at center
        with Dissolve(0.5)
        
        a "{i}I didn’t end up ordering anything extra, but I still got so full from finishing Lis’ leftovers.{/i}"
        
        c "Are you okay, Alice?"
        
        l "Oh, she'll be fine. Just need to work it all off!"
        
        a "{i}Yeah. So what should I do to work this off?{/i}"
        
        #### call screen
        
        
        
        
        
        
label leisurely:
    
    $ leisurelylunch = renpy.random.randint(1,5)
    
    if leisurelylunch == 1:
        
        scene dinnerday
        with fade
        
        show a smile at right
        show m frown at center
        show k smile at left
        with Dissolve(0.5)
        
        a "{i}I return to the dining hall for lunch to see that Mary and Boss are also having their meals.{/i}"
        
        show m talk at center
        show a frown at right
        
        m "Do you always have to raise such a ruckus, Alice?"
        
        show m frown at center
        
        a "{i}I look around to confirm that nobody is anywhere near me.{/i}"
        
        show a shock at right
        
        a "What ruckus?"
        
        show m talk at center
        
        m "The eternal battle between your shoes and the marble floors. Can’t you just step in gently and not make those horrific screeching noises? I would’ve thought somebody just got murdered."
        
        show m frown at center
        show a frown at right
        
        a "{i}That's a bit of an exxageration, right?{/i}"
        a "{i}Whatever. I’ll just order my food and get on with the rest of my afternoon. I’ve gotta get better at performing if I were to stand a chance against everybody else.{/i}"
        a "{i}I start on my quinoa and kale salad topped with jumbo prawns, cranberries, and almond slices, only to have Boss shake her head and tisk at me.{/i}"
        
        k "You never learn, do you?"
        
        show a shock at right
        
        a "Learn what?"
        
        show a frown at right
        
        k "How to live life. Slow down. Enjoy each bite."
        
        show m talk at center
        
        m "That’s what I was getting at. Show some respect to the quinoa."
        
        show m smile at center
        
        a "{i}Respect for quinoa? I feel like holding a seed up to the chandelier light while I offer a prayer to its divine spirit.{/i}"
        a "{i}Nevermind. That would be overdoing it.{/i}"
        a "{i}I swallow the seed on my fork, then pick up another one and lick it into my mouth. I roll the seed around with my tongue before slowly swallowing it down my esophagus.{/i}"
        a "{i}Not like it changes the taste of anything, but it’s sort of relaxing eating at this pace.{/i}"
        
        k "So, Busybody, how will you make your afternoon productive, today?"
        
        
        
        
        
label busy:
    
    $ busylunch = renpy.random.randint(1,5)
    
    if busylunch == 1:
        
        scene dinnerday
        with fade
        
        show a shock at right
        show g smile at left
        show d smile at center
        with Dissolve(0.5)
        
        a "{i}I’m running so late! I better order something, finish it quick, then get on with my training for the afternoon!{/i}"
        
        show g talk at left
        
        g "You okay, Alice?"
        
        show g smile at left
        show a sing at right
        
        a "Yeah, just need to stuff my face and get working."
        
        show a smile at right
        show d talk at center
        
        dir "Young people these days...can’t even manage their time."
        
        show d smile at center
        
        a "{i}How old are you, anyway?{/i}"
        a "{i}My seared ahi tuna steak with crispy wonton chips arrive at that moment. It’s such a waste to gobble the fine food without even tasting it carefully, but whatever… I want to get away from the Director’s glare ASAP.{/i}"
        
        show g talk at left
        
        g "Where are you going after you finish your meal? I’ll walk you there."
        
        show g smile at left
        show a sing at right
        
        a "Sure, thanks."
        a "I'm going to go to..."
        
        ########## call screen
        















