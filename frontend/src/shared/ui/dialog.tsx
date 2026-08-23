import * as React from "react"

import * as DialogPrimitive from "@radix-ui/react-dialog"




import {
  cn,
} from "@/shared/lib/utils"



const Dialog =
  DialogPrimitive.Root



const DialogTrigger =
  DialogPrimitive.Trigger



const DialogPortal =
  DialogPrimitive.Portal



const DialogClose =
  DialogPrimitive.Close



const DialogOverlay = React.forwardRef<any, any>(

({
className,
...props
}, ref) => (

<DialogPrimitive.Overlay

ref={ref}

className={cn(

`
fixed
inset-0
z-40
bg-black/50
`,

className

)}

{...props}

/>

))


DialogOverlay.displayName =
"DialogOverlay"





const DialogContent = React.forwardRef<any, any>(

({

className,

children,

...props

}, ref) => (

<DialogPortal>


<DialogOverlay />



<DialogPrimitive.Content

ref={ref}

className={cn(

`

fixed

left-1/2

top-1/2

z-50

w-[calc(100%-2rem)]

max-w-md

-translate-x-1/2

-translate-y-1/2


rounded-3xl


bg-white


p-8


shadow-2xl


dark:bg-slate-900


`,

className

)}

{...props}

>

{children}

</DialogPrimitive.Content>



</DialogPortal>

))


DialogContent.displayName =
"DialogContent"






const DialogHeader = ({

className,

...props

}: React.HTMLAttributes<HTMLDivElement>) => (

<div

className={cn(

`

mb-6

space-y-3

text-center

`,

className

)}

{...props}

/>

)






const DialogTitle = React.forwardRef<any, any>(

({

className,

...props

}, ref)=>(


<DialogPrimitive.Title

ref={ref}

className={cn(

`

text-2xl

font-bold

text-[#0f2747]

dark:text-white

`,

className

)}

{...props}

/>


))


DialogTitle.displayName =
"DialogTitle"






const DialogDescription = React.forwardRef<any, any>(

({

className,

...props

}, ref)=>(


<DialogPrimitive.Description

ref={ref}

className={cn(

`

text-sm

text-muted-foreground

`,

className

)}

{...props}

/>


))


DialogDescription.displayName =
"DialogDescription"






export {

Dialog,

DialogTrigger,

DialogPortal,

DialogClose,

DialogOverlay,

DialogContent,

DialogHeader,

DialogTitle,

DialogDescription,

}
