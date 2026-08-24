import {
  ArrowLeft,
  CalendarDays,
} from "lucide-react"



import {
  useNavigate,
} from "react-router"



import type {
  Post,
} from "@/entities/blog"





export function PostCard({

  post,

}: {

  post: Post

}) {


  const navigate = useNavigate()



  return (

    <article

      onClick={() =>
        navigate(`/blog/${post.id}`)
      }

      className="

      group

      cursor-pointer

      overflow-hidden

      rounded-3xl

      border

      border-border

      bg-card

      transition-all

      duration-300

      hover:-translate-y-2

      hover:shadow-2xl

      "

    >



      <div

        className="

        h-32

        bg-gradient-to-br

        from-primary/20

        via-primary/10

        to-transparent

        "

      />




      <div

        className="

        space-y-4

        p-5

        "

      >



        <h2

          className="

          line-clamp-2

          text-lg

          font-black

          leading-8

          "

        >

          {post.title}

        </h2>




        <p

          className="

          line-clamp-2

          text-sm

          leading-7

          text-muted-foreground

          "

        >

          {post.content}

        </p>





        <div

          className="

          flex

          items-center

          justify-between

          pt-2

          text-xs

          text-muted-foreground

          "

        >



          <span

            className="

            flex

            items-center

            gap-2

            "

          >

            <CalendarDays size={14}/>

            {post.created_at}

          </span>





          <span

            className="

            flex

            items-center

            gap-1

            font-bold

            text-primary

            opacity-0

            transition-all

            duration-300

            group-hover:opacity-100

            "

          >

            مطالعه

            <ArrowLeft size={15}/>


          </span>



        </div>



      </div>



    </article>

  )

}
