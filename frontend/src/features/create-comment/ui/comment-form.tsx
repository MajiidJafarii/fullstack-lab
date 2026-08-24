import {
  useForm,
} from "react-hook-form"



import {
  zodResolver,
} from "@hookform/resolvers/zod"



import {
  commentSchema,
  type CommentFormValues,
} from "../model/schema"



import {
  useCreateComment,
} from "../model/use-create-comment"





export function CommentForm({

  postId,

}: {

  postId: number

}) {



  const {

    register,

    handleSubmit,

    reset,

    formState: {

      errors,

    },

  } = useForm<CommentFormValues>({

    resolver:

      zodResolver(
        commentSchema
      ),

  })





  const mutation =
    useCreateComment()





  function submit(

    values: CommentFormValues

  ) {


    mutation.mutate(

      {

        data: {

          post:

            postId,

          content:

            values.content,

        },

      },

      {

        onSuccess() {

          reset()

        },

      }

    )


  }





  return (

    <form

      dir="rtl"

      onSubmit={

        handleSubmit(submit)

      }

      className="

      space-y-4

      rounded-3xl

      border

      border-border

      bg-card

      p-6

      "

    >



      <h3

        className="

        text-xl

        font-black

        "

      >

        ارسال دیدگاه

      </h3>




      <textarea

        {...register(
          "content"
        )}

        rows={5}

        placeholder="نظر خود را بنویسید..."

        className="

        w-full

        rounded-2xl

        border

        border-border

        bg-background

        p-4

        outline-none

        focus:ring-2

        focus:ring-primary

        "

      />




      {

        errors.content &&

        (

          <p className="text-sm text-red-500">

            {
              errors.content.message
            }

          </p>

        )

      }




      <button

        disabled={mutation.isPending}

        className="

        rounded-2xl

        bg-primary

        px-6

        py-3

        font-bold

        text-primary-foreground

        disabled:opacity-50

        "

      >

        {

          mutation.isPending

          ?

          "در حال ارسال..."

          :

          "ارسال دیدگاه"

        }


      </button>



    </form>

  )

}
