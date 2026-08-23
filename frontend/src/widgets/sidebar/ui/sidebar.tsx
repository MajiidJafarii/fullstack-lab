import {
  useState,
} from "react"


import {
  NavLink,
  useNavigate,
} from "react-router"



import {
  Home,
  LayoutDashboard,
  User,
  Settings,
  LogOut,
  Menu,
  X,
  FileText,
} from "lucide-react"



import {
  Button,
} from "@/shared/ui/button"



import {
  useAuth,
} from "@/entities/session"



const menuItems = [

  {
    title: "خانه",
    path: "/",
    icon: Home,
  },


  {
    title: "داشبورد",
    path: "/dashboard",
    icon: LayoutDashboard,
  },


  {
    title: "بلاگ",
    path: "/blog",
    icon: FileText,
  },


  {
    title: "پروفایل",
    path: "/profile",
    icon: User,
  },


  {
    title: "تنظیمات",
    path: "/settings",
    icon: Settings,
  },

]




export function Sidebar() {


  const {
    authenticated,
    logout,
  } = useAuth()



  const navigate =
    useNavigate()



  const [
    open,
    setOpen,
  ] = useState(false)



  if (!authenticated) {

    return null

  }



  async function handleLogout() {

    await logout()

    navigate("/")

  }




  return (

    <>


      <Button

        size="icon"

        onClick={() =>
          setOpen(true)
        }

        className="
        fixed
        right-5
        top-5
        z-50
        h-12
        w-12
        rounded-2xl
        bg-[#0f2747]
        text-white
        shadow-xl
        hover:bg-[#163b68]
        "

      >

        <Menu size={22}/>

      </Button>





      {
        open &&

        <div

          className="
          fixed
          inset-0
          z-40
          bg-black/40
          "

          onClick={() =>
            setOpen(false)
          }

        />

      }





      <aside

        className={`
        fixed
        right-0
        top-0
        z-50
        flex
        h-screen
        w-80
        flex-col
        rounded-l-3xl
        border-l
        border-[#d4af37]/50
        bg-[#0f2747]
        p-6
        text-white
        shadow-2xl
        transition-transform
        duration-300

        ${
          open
          ? "translate-x-0"
          : "translate-x-full"
        }

        `}

      >




        <div

          className="
          mb-10
          flex
          items-center
          justify-between
          "

        >

          <div>

            <h2 className="
            text-xl
            font-bold
            ">

              سامانه مدیریت

            </h2>


            <p className="
            mt-1
            text-sm
            text-slate-300
            ">

              پنل کاربری

            </p>

          </div>




          <Button

            size="icon"

            variant="ghost"

            onClick={() =>
              setOpen(false)
            }

            className="
            text-white
            hover:bg-white/10
            "

          >

            <X size={22}/>

          </Button>


        </div>





        <nav className="
        flex-1
        space-y-3
        ">


          {
            menuItems.map(

              (item) => {


                const Icon =
                  item.icon



                return (

                  <NavLink

                    key={item.path}

                    to={item.path}

                    onClick={() =>
                      setOpen(false)
                    }


                    className={({isActive}) => `

                    flex
                    items-center
                    gap-4
                    rounded-2xl
                    px-4
                    py-3
                    text-sm
                    font-medium
                    transition-all

                    ${
                      isActive

                      ?

                      "bg-[#d4af37] text-[#0f2747] shadow-lg"

                      :

                      "text-slate-200 hover:bg-white/10"

                    }

                    `}


                  >

                    <Icon size={21}/>

                    {item.title}


                  </NavLink>

                )

              }

            )

          }


        </nav>






        <Button

          onClick={handleLogout}

          className="
          mt-auto
          h-12
          rounded-2xl
          bg-[#b91c1c]
          text-white
          shadow-lg
          hover:bg-[#991b1b]
          "

        >

          <LogOut size={20}/>

          خروج


        </Button>



      </aside>


    </>

  )
}
