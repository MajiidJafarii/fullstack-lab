import {
  useState,
} from "react"


import {
  Button,
} from "@/shared/ui/button"


import {
  Input,
} from "@/shared/ui/input"


import {
  Textarea,
} from "@/shared/ui/textarea"


import {
  useUpdatePost,
} from "../model/use-update-post"





export function UpdatePostForm({

  postId,

}: {

  postId: number

}) {


  const {
    updatePost,
    isPending,
  } = useUpdatePost()



  const [
    title,
    setTitle,
  ] = useState("")



  const [
    content,
    setContent,
  ] = useState("")





  async function submit(

    e: React.FormEvent

  ) {


    e.preventDefault()



    await updatePost({

      id: postId,

      data: {

        title,

        content,

      },

    })

  }





  return (

    <form

      onSubmit={submit}

      className="
      space-y-4
      rounded-xl
      border
      p-5
      "

    >

      <Input

        placeholder="عنوان جدید"

        value={title}

        onChange={
          e =>
            setTitle(e.target.value)
        }

      />



      <Textarea

        placeholder="محتوای جدید"

        value={content}

        onChange={
          e =>
            setContent(e.target.value)
        }

      />



      <Button

        disabled={isPending}

      >

        ذخیره تغییرات

      </Button>


    </form>

  )

}
