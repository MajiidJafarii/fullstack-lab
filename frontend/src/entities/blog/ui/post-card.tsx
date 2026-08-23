import {
  ArrowLeft,
  CalendarDays,
} from "lucide-react"


import type {
  Post,
} from "@/entities/blog"





export function PostCard({

  post,

}: {

  post: Post

}) {


  return (

    <article

      className="

      group

      relative

      overflow-hidden

      rounded-3xl

      border

      border-border

      bg-card

      text-card-foreground

      shadow-md

      transition-all

      duration-500

      hover:-translate-y-2

      hover:shadow-2xl

      "

    >


      <div

        className="

        h-52

        flex

        items-center

        justify-center

        bg-muted

        transition-transform

        duration-700

        group-hover:scale-110

        "

      >

        بدون تصویر

      </div>





      <div

        className="

        space-y-4

        p-5

        "

      >

        <h2

          className="

          text-xl

          font-bold

          "

        >

          {post.title}

        </h2>




        <p

          className="

          line-clamp-3

          text-sm

          text-muted-foreground

          "

        >

          {post.content}

        </p>




        <div

          className="

          flex

          items-center

          gap-2

          text-xs

          text-muted-foreground

          "

        >

          <CalendarDays size={15}/>

          {post.created_at}

        </div>


      </div>





      <div

        className="

        absolute

        inset-0

        flex

        translate-y-full

        flex-col

        items-center

        justify-center

        gap-6

        bg-gradient-to-br

        from-[#0f2747]/95

        via-[#163b68]/95

        to-[#d4af37]/90

        px-6

        text-white

        backdrop-blur-xl

        transition-all

        duration-500

        group-hover:translate-y-0

        "

      >



        <h3

          className="

          text-center

          text-2xl

          font-black

          "

        >

          {post.title}

        </h3>




        <p

          className="

          text-sm

          text-white/80

          "

        >

          مشاهده جزئیات مطلب

        </p>




        <button

          className="

          flex

          items-center

          gap-3

          rounded-2xl

          border

          border-[#d4af37]

          bg-[#0f2747]/80

          px-8

          py-3

          font-bold

          text-[#d4af37]

          ring-2

          ring-[#d4af37]/40

          shadow-xl

          transition-all

          hover:scale-110

          "

        >

          مطالعه مطلب

          <ArrowLeft size={20}/>

        </button>


      </div>


    </article>

  )

}
