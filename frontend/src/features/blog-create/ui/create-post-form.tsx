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
  useCreatePost,
} from "../model/use-create-post"





export function CreatePostForm() {


  const {
    createPost,
    isPending,
    error,
  } = useCreatePost()



  const [
    title,
    setTitle,
  ] = useState("")



  const [
    content,
    setContent,
  ] = useState("")



  const [
    tags,
    setTags,
  ] = useState("")





  async function submit(

    e: React.FormEvent

  ) {


    e.preventDefault()



    await createPost({

      data: {

        title,

        content,

        status: "published",

        tags: tags
          .split(",")

          .map(

            item => item.trim()

          )

          .filter(Boolean),

      },

    })


  }





  return (

    <form

      onSubmit={submit}

      className="
      space-y-5
      rounded-2xl
      border
      p-6
      "

    >


      <Input

        placeholder="عنوان"

        value={title}

        onChange={
          e =>
            setTitle(
              e.target.value
            )
        }

      />



      <Textarea

        placeholder="محتوا"

        value={content}

        onChange={
          e =>
            setContent(
              e.target.value
            )
        }

      />



      <Input

        placeholder="تگ‌ها با , جدا شوند"

        value={tags}

        onChange={
          e =>
            setTags(
              e.target.value
            )
        }

      />


{
  error ? (

    <p className="text-red-500">

      خطا در ثبت پست

    </p>

  ) : null
}



      <Button

        disabled={isPending}

      >

        {
          isPending

          ?

          "در حال ثبت..."

          :

          "ثبت پست"

        }

      </Button>


    </form>

  )

}
