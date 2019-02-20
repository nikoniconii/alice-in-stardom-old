######################### Which type of day will it be?

label whatday:

    ## variable daytype is randomized
    
    $ daytype = renpy.random.randint(1,4)
    
    if daytype == 1:
        
        jump normal
        
    if daytype == 2:
        
        jump hopeful
        
    if daytype == 3:
        
        jump anxious
        
    if daytype == 4:
        
        jump tired


######################### Normal Wake-up

label normal:
    
    $ normalday = renpy.random.randint(1)
    
    if normalday == 1:
        
        scene bedaliceday
        with fade
        
        show a smile
        with Dissolve(0.5)
        
        a "{i}Ahh, it's morning.{/i}"
        a "{i}I can't recall my dreams, so I must've had some decent sleep. I feel rested enough.{/i}"
        a "{i}Wow, I didn't even know my back could crack that much! These beds are really amazing. Alright, time to go to the washroom and make myself presentable before breakfast.{/i}"
        
        scene dinnerday
        with fade
        
        show a smile at right
        show g smile at left
        show j smile at center
        with Dissolve(0.5)
        
        show g talk at left
        
        g "Good morning."
        
        show g smile at left
        show a sing at right
        
        a "Morning."
        
        show a smile at right
        show j talk at center
        
        j "How are you feeling today?"
        
        show a sing at right
        show j smile at center
        
        a "I guess I'm fine. What's for breakfast?"
        
        show j talk at center
        
        j "Here's the selection for today."
        
        show j smile at center
        
        a "{i}I'm still not really used to ordering from a menu. It's like eating at a restaurant, except you don't have to pay the bill!{/i}"
        a "{i}Weird.{/i}"
        
        show a cute at right
        
        a "I'll have some pancakes!"
        
        a "{i}As always, they're delicious. It doesn't take long before I gobble it all up.{/i}"
        
        show j talk at center
        
        j "Now that you're done, what are you going to do the rest of the morning?"
        
#    if normalday == 2:
        
        
        

label hopeful:
    
    $ hopefulday = renpy.random.randint(1,5)
    
    if hopefulday == 1:
        
        scene bedaliceday
        with fade
        
        show a cute
        with Dissolve(0.5)
        
        a "{i}I awake to the first light of day streaming through my curtains.{/i}"
        a "{i}My alarm has yet to sound. I turn it off, feeling rested enough that I don't need to sleep in any longer.{/i}"
        a "{i}The air smells fresh. I take a deep breath in, letting the oxygen fill every cell in my body.{/i}"
        a "{i}It’s a new day, and with it, a new adventure awaits. Just thinking about all that has happened is making me excited!{/i}"
        a "{i}Yeah, I’m nervous, but I think I’m happy. Let’s try hard today too!{/i}"
        
        scene dinnerday
        with fade
        
        show a cute at right
        show l smile at left
        show c cute at center
        with Dissolve(0.5)
        
        l "Mornin'"
        
        show a sing at right
        
        a "Good morning, Lis."
        
        show a smile at right
        
        l "You look like you're ready to rock the world!"
        
        show a sing at right
        
        a "Not sure about that, but I do feel sorta upbeat today."
        
        show a cute at right
        show c talk at center
        
        c "That’s good to hear. You’ll feel even better after you’ve filled your stomach. The piggy sausages are delicious!"
        
        show c cute at center
        
        a "{i}I guess I’ll go for the pork sausages with hash browns this morning too. Those would go well with a fresh fruit salad and Greek yogurt to round it all up. Gosh, with an appetite like this, I’m gonna get real fat in no time!{/i}"
        a "{i}Not that I mind a little extra weight. My mom keeps saying I'm not eating enough.{/i}"
        
        l "So what are you up to this morning?"
        
        #### call screen
        



label anxious:
    
    $ anxiousday = renpy.random.randint(1,5)
    
    if anxiousday == 1:
        
        scene bedaliceday
        with fade
        
        show a frown
        with Dissolve(0.5)
        
        a "{i}I have been tossing and turning the entire night. For some reason, I couldn't sleep.{/i}"
        a "{i}The sun has finally risen. I turn off the alarm I set and drag myself out of bed.{/i}"
        a "{i}No matter how many times I look at it, this room still feels so empty. Sure, there's pieces of high-class furniture to fill the space in an artsy arrangement, it’s still much too large a place for a single person to stay in.{/i}"
        a "{i}I don't belong here, do I?{/i}"
        a "{i}What the hell am I thinking? I must be having one of those days. Time to gather myself before heading down for breakfast.{/i}"
        
        scene dinnerday
        with fade
        
        show a frown at right
        show d smile at left
        show t frown at center
        with Dissolve(0.5)
        
        show t frowntalk at center
        
        t "You look like a zombie."
        
        show t frown at center
        
        a "I'm sure you're right."
        
        a "{i}Not that I exactly want to hear it from you.{/i}"
        
        show d talk at left
        
        di "Eat up and get yourself together, Intie."
        
        a "{i}The director slides the menu across the table. I don’t bother with it, just turning around to the maid to ask her for a glass of water and a piece of toast. I don’t have much of an appetite for anything else.{/i}"
        a "{i}Ordering for food is just one of the many strange ways things are done here. It feels so alien.{/i}"
        
        show t frowntalk at center
        
        t "Better that you keep yourself preoccupied than to worry about unnecessary things."
        
        show t frown at center
        
        a "{i}Yeah, I guess he's right. What should I do this morning?{/i}"
    
        
    


label tired:
    
    $ tiredday = renpy.random.randint(1,5)
    
    if tiredday == 1:
        
        scene bedaliceday
        with fade
        
        show a frown
        with Dissolve(0.5)
        
        a "{i}What's that?{/i}"
        a "{i}It takes a moment before my groggy mind can register the sound from my bedside. I reach an arm out to slam on the alarm clock before shrinking back under the sheets.{/i}"
        a "{i}Cold... it's so cold out.{/i}"
        a "{i}It's a lot warmer here. I still want to sleep.{/i}"
        a "{i}Just five more minutes... I'll wake up after that...{/i}"
        
        scene bedaliceday
        with fade
        
        with hpunch
        
        a "{i}Shit! I've slept an extra hour!{/i}"
        a "{i}I'm so late for breakfast. I better get going!{/i}"
        
        scene dinnerday
        with fade
        
        show a frown at right
        show m frown at center
        show k smile at left
        with Dissolve(0.5)
        
        show m sing at center
        
        m "Someone hasn't had a good night's sleep."
        
        show m frown at center
        
        a "Just a little tired, is all."
        
        k "Tiredness is the worst enemy for a woman's beauty."
        
        a "{i}For anybody's health for that matter. Not like I actually want to be so tired...sheesh.{/i}"
        
        show m sing at center
        
        m "The air circulation system in this building needs work. We can adjust the temperature in our own rooms, but not the humidity. What blasphemy!"
        
        show m frown at center
        
        a "{i}Yes, Mary. We know you like to complain, but that’s really a non-complaint, okay? My whole apartment building back home has a single temperature control!{/i}"
        
        a "Whatever. If there’s a second enemy for a woman’s beauty, it’s an empty stomach."
        a "I'll have some ice-cream waffles!"
        
        a "{i}Maybe the sweets will help improve my mood for the morning.{/i}"
        a "{i}Now what should I do for the rest of the day before lunch?{/i}"
        
        #### call screen
        



    
    
    
    
    
    
    
    