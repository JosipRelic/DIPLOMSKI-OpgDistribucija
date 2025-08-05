<template>
  <aside class="w-full h-full min-h-screen bg-white p-10 flex flex-col justify-between">
    <div>
      <div
        class="group flex items-center pr-3 py-2 text-sm text-gray-600 rounded-lg justify-between cursor-pointer"
      >
        <span class="flex items-center">
          <img
            class="mr-3 w-10 h-10 object-cover rounded-full"
            src="https://images.unsplash.com/photo-1660412230160-9bc219efcb00?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8bWFsZSUyMHNob3BwZXJ8ZW58MHx8MHx8fDI%3D"
            alt=""
          />
          <p class="flex flex-col">
            <span class="text-sm text-black font-bold">
              Ivan Horvat <span class="text-sm text-gray-400">(Kupac)</span>
            </span>
            <span class="text-sm">ihorvat@gmail.com</span>
          </p>
        </span>
      </div>
      <nav class="md:mt-10 mt-5">
        <ul class="space-y-3 border-b border-gray-200 pb-3">
          <li>
            <router-link
              :to="{ name: 'profilKupacNadzornaPloca' }"
              class="group flex items-center px-3 py-2 text-sm text-gray-600 hover:bg-[#223c2f] hover:text-white rounded-lg"
              :class="{ 'bg-[#223c2f] text-white': $route.name === 'profilKupacNadzornaPloca' }"
            >
              <svg
                class="mr-3 stroke-gray-500 group-hover:stroke-white"
                width="24"
                height="25"
                viewBox="0 0 24 25"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <g clip-path="url(#clip0_4787_2976)">
                  <path
                    d="M21 19.7725H3V4.77246"
                    stroke="currentColor"
                    stroke-width="1.5"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                  <path
                    d="M19.5 6.27246L12 13.7725L9 10.7725L3 16.7725"
                    stroke="currentColor"
                    stroke-width="1.5"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                  <path
                    d="M19.5 10.0225V6.27246H15.75"
                    stroke="currentColor"
                    stroke-width="1.5"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                </g>
                <defs>
                  <clipPath id="clip0_4787_2976">
                    <rect y="0.272461" width="24" height="24" rx="4" fill="currentColor" />
                  </clipPath>
                </defs>
              </svg>
              Nadzorna ploča
            </router-link>
          </li>

          <li>
            <router-link
              :to="{ name: 'profilKupacMojeNarudzbe' }"
              class="group flex items-center px-3 py-2 text-sm text-gray-600 hover:bg-[#223c2f] hover:text-white rounded-lg"
              :class="{ 'bg-[#223c2f] text-white': $route.name === 'profilKupacMojeNarudzbe' }"
            >
              <div class="justify-between">
                <span class="flex items-center">
                  <svg
                    class="mr-3 stroke-gray-500 group-hover:stroke-white"
                    width="24"
                    height="25"
                    viewBox="0 0 24 25"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M21 16.8945V7.6507C20.9993 7.51718 20.9634 7.38621 20.8959 7.27099C20.8284 7.15577 20.7317 7.06039 20.6156 6.99445L12.3656 2.35383C12.2545 2.28965 12.1284 2.25586 12 2.25586C11.8716 2.25586 11.7455 2.28965 11.6344 2.35383L3.38437 6.99445C3.26827 7.06039 3.1716 7.15577 3.10411 7.27099C3.03663 7.38621 3.00072 7.51718 3 7.6507V16.8945C3.00072 17.028 3.03663 17.1589 3.10411 17.2742C3.1716 17.3894 3.26827 17.4848 3.38437 17.5507L11.6344 22.1913C11.7455 22.2555 11.8716 22.2893 12 22.2893C12.1284 22.2893 12.2545 22.2555 12.3656 22.1913L20.6156 17.5507C20.7317 17.4848 20.8284 17.3894 20.8959 17.2742C20.9634 17.1589 20.9993 17.028 21 16.8945V16.8945Z"
                      stroke="currentColor"
                      stroke-width="1.5"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                    />
                    <path
                      d="M16.5938 14.5693V9.69434L7.5 4.67871"
                      stroke="currentColor"
                      stroke-width="1.5"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                    />
                    <path
                      d="M20.8953 7.2666L12.0828 12.2729L3.10156 7.2666"
                      stroke="currentColor"
                      stroke-width="1.5"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                    />
                    <path
                      d="M12.0844 12.2725L12 22.285"
                      stroke="currentColor"
                      stroke-width="1.5"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                    />
                  </svg>
                  Moje narudžbe
                </span>
              </div>
            </router-link>
          </li>

          <li>
            <router-link
              :to="{ name: 'profilKupacPostavke' }"
              class="group flex items-center px-3 py-2 text-sm text-gray-600 hover:bg-[#223c2f] hover:text-white rounded-lg"
              :class="{ 'bg-[#223c2f] text-white': $route.name === 'profilKupacPostavke' }"
            >
              <div class="justify-between">
                <span class="flex items-center">
                  <svg
                    class="mr-3 stroke-gray-500 group-hover:stroke-white"
                    width="24"
                    height="25"
                    viewBox="0 0 24 25"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M12 16.7725C14.4853 16.7725 16.5 14.7577 16.5 12.2725C16.5 9.78718 14.4853 7.77246 12 7.77246C9.51472 7.77246 7.5 9.78718 7.5 12.2725C7.5 14.7577 9.51472 16.7725 12 16.7725Z"
                      stroke="currentColor"
                      stroke-width="1.5"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                    />
                    <path
                      d="M18.5071 7.83769C18.7328 8.16083 18.9304 8.5027 19.0978 8.85957L21.5259 10.2096C21.8291 11.5675 21.8323 12.9753 21.5353 14.3346L19.0978 15.6846C18.9304 16.0414 18.7328 16.3833 18.5071 16.7064L18.554 19.4908C17.525 20.4285 16.307 21.135 14.9821 21.5627L12.5915 20.1283C12.1983 20.1565 11.8035 20.1565 11.4103 20.1283L9.02901 21.5533C7.69992 21.1334 6.47797 20.4297 5.44776 19.4908L5.49463 16.7158C5.27082 16.3882 5.07333 16.0434 4.90401 15.6846L2.47588 14.3346C2.17269 12.9766 2.16949 11.5689 2.46651 10.2096L4.90401 8.85957C5.07133 8.5027 5.26893 8.16083 5.49463 7.83769L5.44776 5.05332C6.4768 4.1156 7.69474 3.40913 9.01963 2.98145L11.4103 4.41582C11.8035 4.38769 12.1983 4.38769 12.5915 4.41582L14.9728 2.99082C16.3018 3.41072 17.5238 4.11446 18.554 5.05332L18.5071 7.83769Z"
                      stroke="currentColor"
                      stroke-width="1.5"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                    />
                  </svg>
                  Postavke profila
                </span>
              </div>
            </router-link>
          </li>
        </ul>
        <ul class="space-y-3 pt-3">
          <li
            class="group flex items-center px-3 py-2 text-sm text-red-500 hover:bg-red-500 justify-between hover:text-white rounded-lg cursor-pointer"
          >
            <span class="flex items-center">
              <svg
                class="mr-3 stroke-gray-500 group-hover:stroke-white"
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="25"
                viewBox="0 0 16 16"
              >
                <path
                  fill="currentColor"
                  d="M12 1c1.1 0 2 .895 2 2v9c0 1.1-.895 2-2 2H9.5a.5.5 0 0 1 0-1H12a1 1 0 0 0 1-1V3a1 1 0 0 0-1-1H9.5a.5.5 0 0 1 0-1z"
                  stroke="currentColor"
                  stroke-width="0.5"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  fill="currentColor"
                  d="M4.15 4.15a.5.5 0 0 1 .707.707l-2.15 2.15h6.79a.5.5 0 0 1 0 1h-6.79l2.15 2.15a.5.5 0 0 1-.707.707l-3-3a.5.5 0 0 1 0-.707l3-3z"
                  stroke="currentColor"
                  stroke-width="0.5"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </svg>
              Odjava
            </span>
          </li>
        </ul>
      </nav>
    </div>
  </aside>
</template>
