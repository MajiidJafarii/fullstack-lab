import * as React from "react"

import {
  cva,
  type VariantProps,
} from "class-variance-authority"

import {
  cn,
} from "@/shared/lib/utils"



const buttonVariants = cva(

  `
  inline-flex
  items-center
  justify-center
  gap-2

  whitespace-nowrap

  rounded-xl

  text-sm
  font-medium

  transition-all
  duration-200

  outline-none

  disabled:pointer-events-none
  disabled:opacity-50

  focus-visible:ring-2
  focus-visible:ring-ring

  cursor-pointer
  `,

  {

    variants: {

      variant: {

        default: `
          bg-primary
          text-primary-foreground
          shadow-md
          hover:-translate-y-0.5
          hover:shadow-lg
        `,

        destructive: `
          bg-destructive
          text-white
          hover:opacity-90
        `,

        outline: `
          border
          bg-background
          shadow-sm
          hover:bg-accent
          hover:-translate-y-0.5
        `,

        secondary: `
          bg-secondary
          text-secondary-foreground
          hover:bg-secondary/80
        `,

        ghost: `
          hover:bg-accent
        `,

        link: `
          text-primary
          underline-offset-4
          hover:underline
        `,

      },


      size: {

        default: `
          h-10
          px-5
        `,

        sm: `
          h-9
          px-3
        `,

        lg: `
          h-12
          px-8
        `,

        icon: `
          h-10
          w-10
        `,

        "icon-sm": `
          h-8
          w-8
        `,

        "icon-xs": `
          h-7
          w-7
        `,

      },

    },


    defaultVariants: {

      variant: "default",

      size: "default",

    },

  }

)



type ButtonProps =

React.ButtonHTMLAttributes<HTMLButtonElement>

& VariantProps<typeof buttonVariants>

& {

  asChild?: boolean

  render?: React.ReactElement<any>

  nativeButton?: boolean

}



export function Button({

  className,

  variant,

  size,

  render,

  ...props

}: ButtonProps) {


  const classes = cn(

    buttonVariants({

      variant,

      size,

    }),

    className

  )



  if (render) {


    return React.cloneElement<any>(

      render,

      {

        ...props,

        className: classes,

      }

    )

  }




  return (

    <button

      className={classes}

      {...props}

    />

  )

}



export {

  buttonVariants,

}
