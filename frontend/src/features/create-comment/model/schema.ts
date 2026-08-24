import {
  z,
} from "zod"



export const commentSchema = z.object({

  content:

    z.string()

    .min(
      5,
      "کامنت باید حداقل ۵ کاراکتر باشد"
    )

    .max(
      1000,
      "کامنت نباید بیشتر از ۱۰۰۰ کاراکتر باشد"
    ),

})



export type CommentFormValues =
  z.infer<typeof commentSchema>
